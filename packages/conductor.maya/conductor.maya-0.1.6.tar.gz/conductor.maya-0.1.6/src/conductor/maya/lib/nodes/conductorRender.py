import glob
import imp
import json
import os
import re

import maya.api.OpenMaya as om
import pymel.core as pm
from conductor.core.expander import Expander
from conductor.core.gpath_list import PathList
from conductor.core.package_environment import PackageEnvironment
from conductor.core.sequence import Sequence
from conductor.maya.lib import const as k
from conductor.maya.lib import layer_utils, software


def maya_useNewAPI():
    pass


class conductorRender(om.MPxNode):

    # static attributes
    aTitle = None

    aChunkSize = None
    aUseCustomRange = None
    aCustomRange = None
    aStartFrame = None
    aEndFrame = None
    aByFrame = None
    aUseScoutFrames = None
    aScoutFrames = None

    aTaskTemplate = None

    aInstanceTypeName = None
    aPreemptible = None
    aProjectName = None
    aRenderLayers = None
    aHostSoftware = None
    aPluginSoftware = None
    aExtraAssets = None

    aAssetScraperPath = None
    aAssetScraperActive = None
    aAssetScrapers = None

    aExtraEnvironment = None
    aExtraEnvironmentKey = None
    aExtraEnvironmentValue = None
    aExtraEnvironmentExclusive = None

    aMetadata = None
    aMetadataKey = None
    aMetadataValue = None

    aUploadOnly = None
    aUseUploadDaemon = None

    aEmailAddresses = None
    aEmailAddress = None
    aEmailAddressActive = None

    aRetriesWhenPreempted = None
    aRetriesWhenFailed = None

    aTaskLimit = None
    aDoScrape = None

    aFrameCount = None
    aTaskCount = None
    aScoutTaskCount = None
    aAssetCount = None
    aAssetsSize = None
    aFrameSpec = None

    aDestinationDirectory = None
    aLocationTag = None

    aAutosave = None
    aAutosaveTemplate = None
    aCleanupAutosave = None

    aOutput = None
    aForceOutput = None

    id = om.MTypeId(0x880500)

    @staticmethod
    def creator():
        return conductorRender()

    def postConstructor(self):
        """
        Set up some defaults on node creation.

        1. Set a default title expression.
        2. Set the scraper paths.
        3. Connect atts from renderGlobals
        """
        fn_node = om.MFnDependencyNode(self.thisMObject())
        self.set_default_asset_scrapers(fn_node)
        self.set_default_metadata(fn_node)
        self.connect_render_globals_frame_atts(fn_node)

        fn_node.findPlug(self.aTitle, True).setString(k.DEFAULT_TITLE)

        fn_node.findPlug(self.aAutosaveTemplate, True).setString(
            k.DEFAULT_AUTOSAVE_TEMPLATE)

        fn_node.findPlug(self.aTaskTemplate, True).setString(
            k.DEFAULT_TEMPLATE)

        fn_node.findPlug(self.aHostSoftware, True).setString(
            software.detect_host())
        self.detect_plugins(fn_node)

        fn_node.findPlug(self.aCustomRange, True).setString("1-10")
        fn_node.findPlug(self.aScoutFrames, True).setString("1-10x3")

        dest_path = os.path.join(
            pm.workspace(q=True, rd=True),
            pm.workspace.fileRules.get("images")
        )
        fn_node.findPlug(self.aDestinationDirectory, True).setString(dest_path)

    @classmethod
    def detect_plugins(cls, fn_node):
        array_plug = fn_node.findPlug(cls.aPluginSoftware, True)
        i = 0
        mtoa_version = software.detect_mtoa()
        if mtoa_version:
            array_plug.elementByLogicalIndex(i).setString(mtoa_version)
            i += 1

        rfm_version = software.detect_rfm()
        if rfm_version:
            array_plug.elementByLogicalIndex(i).setString(rfm_version)
            i += 1

    @classmethod
    def set_default_asset_scrapers(cls, fn_node):
        plug = fn_node.findPlug(cls.aAssetScrapers, True)
        scrapers_path = os.path.join(
            pm.moduleInfo(
                path=True, moduleName="conductor"), "lib", "scrapers"
        )
        files = sorted(glob.glob("{}/scrape_*.py".format(scrapers_path)))
        for i, scraper in enumerate(files):
            path_plug = plug.elementByLogicalIndex(i).child(
                cls.aAssetScraperPath
            )
            path_plug.setString(scraper)

    @classmethod
    def set_default_metadata(cls, fn_node):
        element_plug =  fn_node.findPlug(cls.aMetadata, True).elementByLogicalIndex(0)
        element_plug.child(cls.aMetadataKey).setString("ConductorVersion")
        element_plug.child(cls.aMetadataValue).setString("<ConductorVersion>")
 

    @classmethod
    def connect_render_globals_frame_atts(cls, fn_node):
        dest_start_plug = fn_node.findPlug(cls.aStartFrame, True)
        dest_end_plug = fn_node.findPlug(cls.aEndFrame, True)
        dest_by_plug = fn_node.findPlug(cls.aByFrame, True)

        sel = om.MSelectionList()
        try:
            sel.add("defaultRenderGlobals.startFrame")
            sel.add("defaultRenderGlobals.endFrame")
            sel.add("defaultRenderGlobals.byFrameStep")
        except BaseException:
            pm.warning("Can't connect defaultRenderGlobals frames attributes.")
        src_start_plug = sel.getPlug(0)
        src_end_plug = sel.getPlug(1)
        src_by_plug = sel.getPlug(2)

        modifier = om.MDGModifier()
        modifier.connect(src_start_plug, dest_start_plug)
        modifier.connect(src_end_plug, dest_end_plug)
        modifier.connect(src_by_plug, dest_by_plug)
        modifier.doIt()

    @classmethod
    def initialize(cls):
        cls.make_title_att()
        cls.make_frames_atts()
        cls.make_instance_type_att()
        cls.make_project_name_att()
        cls.make_layer_att()
        cls.make_software_att()
        cls.make_assets_atts()
        cls.make_environment_atts()
        cls.make_task_atts()
        cls.make_upload_flag_atts()
        cls.make_notification_atts()
        cls.make_metadata_atts()
        cls.make_retries_atts()

        cls.make_hidden_atts()
        cls.make_info_atts()

        cls.make_autosave_atts()

        cls.make_misc_atts()

        cls.make_output_att()

        cls.setup_attribute_affects()

    @staticmethod
    def _make_output_int_att(longname, shortname):
        nAttr = om.MFnNumericAttribute()
        att = nAttr.create(longname, shortname, om.MFnNumericData.kInt)
        nAttr.storable = False
        nAttr.writable = False
        nAttr.readable = True
        om.MPxNode.addAttribute(att)
        return att

    @classmethod
    def make_info_atts(cls):

        cls.aFrameCount = cls._make_output_int_att("frameCount", "frc")
        cls.aTaskCount = cls._make_output_int_att("taskCount", "tsc")
        cls.aScoutTaskCount = cls._make_output_int_att("scoutTaskCount", "stc")
        cls.aAssetCount = cls._make_output_int_att("assetCount", "asc")
        cls.aAssetsSize = cls._make_output_int_att("assetsSize", "asz")

        tAttr = om.MFnTypedAttribute()
        cls.aFrameSpec = tAttr.create("frameSpec", "fms", om.MFnData.kString)
        tAttr.storable = False
        tAttr.writable = False
        tAttr.readable = True
        om.MPxNode.addAttribute(cls.aFrameSpec)

    @classmethod
    def make_title_att(cls):
        tAttr = om.MFnTypedAttribute()
        cls.aTitle = tAttr.create("title", "ttl", om.MFnData.kString)
        tAttr.hidden = False
        tAttr.storable = True
        tAttr.readable = True
        tAttr.writable = True
        om.MPxNode.addAttribute(cls.aTitle)

    @classmethod
    def make_instance_type_att(cls):
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()
        cls.aInstanceTypeName = tAttr.create(
            "instanceTypeName", "itn", om.MFnData.kString
        )
        tAttr.hidden = False
        tAttr.storable = True
        tAttr.readable = True
        tAttr.writable = True
        om.MPxNode.addAttribute(cls.aInstanceTypeName)

        cls.aPreemptible = nAttr.create(
            "preemptible", "prm", om.MFnNumericData.kBoolean, True
        )
        nAttr.keyable = True
        nAttr.storable = True
        nAttr.readable = True
        nAttr.writable = True
        om.MPxNode.addAttribute(cls.aPreemptible)

    @classmethod
    def make_project_name_att(cls):
        tAttr = om.MFnTypedAttribute()
        cls.aProjectName = tAttr.create(
            "projectName", "prn", om.MFnData.kString
        )
        tAttr.hidden = False
        tAttr.storable = True
        tAttr.readable = True
        tAttr.writable = True
        om.MPxNode.addAttribute(cls.aProjectName)

    @classmethod
    def make_layer_att(cls):
        eAttr = om.MFnEnumAttribute()
        cls.aRenderLayers = eAttr.create(
            "renderLayers", "rl", k.CURRENT_LAYER
        )
        eAttr.addField("current", k.CURRENT_LAYER)
        eAttr.addField("renderable", k.RENDERABLE_LAYERS)
        eAttr.hidden = False
        eAttr.keyable = True
        om.MPxNode.addAttribute(cls.aRenderLayers)

    @classmethod
    def make_software_att(cls):
        tAttr = om.MFnTypedAttribute()
        cls.aHostSoftware = tAttr.create(
            "hostSoftware", "hsw", om.MFnData.kString
        )
        tAttr.hidden = False
        tAttr.writable = True
        om.MPxNode.addAttribute(cls.aHostSoftware)

        cls.aPluginSoftware = tAttr.create(
            "pluginSoftware", "psw", om.MFnData.kString
        )
        tAttr.array = True
        tAttr.hidden = False
        tAttr.writable = True
        om.MPxNode.addAttribute(cls.aPluginSoftware)

    @classmethod
    def make_assets_atts(cls):
        cAttr = om.MFnCompoundAttribute()
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()

        cls.aAssetScraperPath = tAttr.create(
            "assetScraperPath", "asp", om.MFnData.kString
        )
        tAttr.usedAsFilename = True

        cls.aAssetScraperActive = nAttr.create(
            "assetScraperActive", "asa", om.MFnNumericData.kBoolean, True
        )

        cls.aAssetScrapers = cAttr.create("assetScrapers", "ascs")
        cAttr.array = True
        cAttr.hidden = False
        cAttr.writable = True
        cAttr.addChild(cls.aAssetScraperPath)
        cAttr.addChild(cls.aAssetScraperActive)
        om.MPxNode.addAttribute(cls.aAssetScrapers)

        conductorRender.aExtraAssets = tAttr.create(
            "extraAssets", "eass", om.MFnData.kString
        )
        tAttr.array = True
        tAttr.hidden = False
        tAttr.writable = True
        tAttr.usedAsFilename = True
        om.MPxNode.addAttribute(conductorRender.aExtraAssets)

    @classmethod
    def make_environment_atts(cls):
        cAttr = om.MFnCompoundAttribute()
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()
        cls.aExtraEnvironmentKey = tAttr.create(
            "extraEnvironmentKey", "eek", om.MFnData.kString
        )
        cls.aExtraEnvironmentValue = tAttr.create(
            "extraEnvironmentValue", "eev", om.MFnData.kString
        )
        cls.aExtraEnvironmentExclusive = nAttr.create(
            "extraEnvironmentExclusive", "eee", om.MFnNumericData.kBoolean, False
        )
        cls.aExtraEnvironment = cAttr.create("extraEnvironment", "een")

        cAttr.hidden = False
        cAttr.writable = True
        cAttr.array = True
        cAttr.addChild(cls.aExtraEnvironmentKey)
        cAttr.addChild(cls.aExtraEnvironmentValue)
        cAttr.addChild(cls.aExtraEnvironmentExclusive)
        om.MPxNode.addAttribute(cls.aExtraEnvironment)

    @classmethod
    def make_metadata_atts(cls):
        cAttr = om.MFnCompoundAttribute()
        tAttr = om.MFnTypedAttribute()
        cls.aMetadataKey = tAttr.create(
            "metadataKey", "mdk", om.MFnData.kString
        )
        cls.aMetadataValue = tAttr.create(
            "metadataValue", "mdv", om.MFnData.kString
        )

        cls.aMetadata = cAttr.create("metadata", "md")

        cAttr.hidden = False
        cAttr.writable = True
        cAttr.array = True
        cAttr.addChild(cls.aMetadataKey)
        cAttr.addChild(cls.aMetadataValue)
        om.MPxNode.addAttribute(cls.aMetadata)

    @classmethod
    def make_retries_atts(cls):
        nAttr = om.MFnNumericAttribute()

        cls.aRetriesWhenFailed = nAttr.create(
            "retriesWhenFailed", "rwf", om.MFnNumericData.kInt, 2
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aRetriesWhenFailed)

        cls.aRetriesWhenPreempted = nAttr.create(
            "retriesWhenPreempted", "rwp", om.MFnNumericData.kInt, 2
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aRetriesWhenPreempted)

    @classmethod
    def make_upload_flag_atts(cls):
        nAttr = om.MFnNumericAttribute()

        cls.aUseUploadDaemon = nAttr.create(
            "useUploadDaemon", "uud", om.MFnNumericData.kBoolean, False
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aUseUploadDaemon)

        conductorRender.aUploadOnly = nAttr.create(
            "uploadOnly", "upo", om.MFnNumericData.kBoolean, False
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(conductorRender.aUploadOnly)

    @classmethod
    def make_frames_atts(cls):
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()
        uAttr = om.MFnUnitAttribute()

        cls.aStartFrame = uAttr.create(
            "startFrame", "stf", om.MFnUnitAttribute.kTime, 1
        )
        uAttr.writable = True
        uAttr.keyable = True
        uAttr.storable = True
        om.MPxNode.addAttribute(cls.aStartFrame)

        cls.aEndFrame = uAttr.create(
            "endFrame", "enf", om.MFnUnitAttribute.kTime, 10
        )
        uAttr.writable = True
        uAttr.keyable = True
        uAttr.storable = True
        om.MPxNode.addAttribute(cls.aEndFrame)

        cls.aByFrame = nAttr.create(
            "byFrame", "byf", om.MFnNumericData.kInt, 1
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aByFrame)

        cls.aChunkSize = nAttr.create(
            "chunkSize", "csz", om.MFnNumericData.kInt, 1
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aChunkSize)

        cls.aUseCustomRange = nAttr.create(
            "useCustomRange", "ucr", om.MFnNumericData.kBoolean, False
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aUseCustomRange)

        cls.aCustomRange = tAttr.create(
            "customRange", "crn", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        om.MPxNode.addAttribute(cls.aCustomRange)

        cls.aUseScoutFrames = nAttr.create(
            "useScoutFrames", "usf", om.MFnNumericData.kBoolean, True
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aUseScoutFrames)

        cls.aScoutFrames = tAttr.create(
            "scoutFrames", "scf", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        om.MPxNode.addAttribute(cls.aScoutFrames)

    @classmethod
    def make_task_atts(cls):
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()
        cls.aTaskTemplate = tAttr.create(
            "taskTemplate", "ttm", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        om.MPxNode.addAttribute(cls.aTaskTemplate)

        cls.aMaxTasksPerJob = nAttr.create(
            "maxTasksPerJob", "mtj", om.MFnNumericData.kInt, 1000
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aMaxTasksPerJob)

    @classmethod
    def make_notification_atts(cls):
        cAttr = om.MFnCompoundAttribute()
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()

        cls.aEmailAddress = tAttr.create(
            "emailAddress", "eml", om.MFnData.kString
        )

        cls.aEmailAddressActive = nAttr.create(
            "emailAddressActive", "emla", om.MFnNumericData.kBoolean, True
        )

        cls.aEmailAddresses = cAttr.create("emailAddresses", "emls")

        cAttr.hidden = False
        cAttr.writable = True
        cAttr.array = True
        cAttr.addChild(cls.aEmailAddress)
        cAttr.addChild(cls.aEmailAddressActive)
        om.MPxNode.addAttribute(cls.aEmailAddresses)

    @classmethod
    def make_misc_atts(cls):
        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()
        cls.aDestinationDirectory = tAttr.create(
            "destinationDirectory", "ddr", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        tAttr.usedAsFilename = True
        om.MPxNode.addAttribute(cls.aDestinationDirectory)

        cls.aLocationTag = tAttr.create(
            "locationTag", "lct", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        om.MPxNode.addAttribute(cls.aLocationTag)

    @classmethod
    def make_autosave_atts(cls):

        tAttr = om.MFnTypedAttribute()
        nAttr = om.MFnNumericAttribute()

        cls.aAutosaveTemplate = tAttr.create(
            "autosaveTemplate", "ast", om.MFnData.kString
        )
        tAttr.writable = True
        tAttr.storable = True
        om.MPxNode.addAttribute(cls.aAutosaveTemplate)

        cls.aAutosave = nAttr.create(
            "autosave", "aus", om.MFnNumericData.kBoolean, True
        )
        nAttr.writable = True
        nAttr.storable = True
        nAttr.hidden = True
        om.MPxNode.addAttribute(cls.aAutosave)

        cls.aCleanupAutosave = nAttr.create(
            "cleanupAutosave", "cua", om.MFnNumericData.kBoolean, True
        )
        nAttr.writable = True
        nAttr.keyable = True
        nAttr.storable = True
        om.MPxNode.addAttribute(cls.aCleanupAutosave)

    @classmethod
    def make_hidden_atts(cls):
        nAttr = om.MFnNumericAttribute()
        cls.aDoScrape = nAttr.create(
            "doScrape", "dsc", om.MFnNumericData.kBoolean, False
        )
        nAttr.writable = True
        nAttr.storable = True
        nAttr.hidden = True
        om.MPxNode.addAttribute(cls.aDoScrape)

        cls.aTaskLimit = nAttr.create(
            "taskLimit", "tsl", om.MFnNumericData.kInt, 10
        )
        nAttr.writable = True
        nAttr.storable = True
        nAttr.hidden = True
        om.MPxNode.addAttribute(cls.aTaskLimit)

    @classmethod
    def make_output_att(cls):
        """
        Output atttribute.
        """
        tAttr = om.MFnTypedAttribute()
        cls.aOutput = tAttr.create("output", "out", om.MFnData.kString)
        tAttr.readable = True
        tAttr.storable = False
        om.MPxNode.addAttribute(cls.aOutput)

    @classmethod
    def setup_attribute_affects(cls):
        om.MPxNode.attributeAffects(cls.aTitle, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aInstanceTypeName, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aProjectName, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aUseCustomRange, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aCustomRange, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aStartFrame, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aEndFrame, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aByFrame, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aUseScoutFrames, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aScoutFrames, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aHostSoftware, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aPluginSoftware, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aExtraEnvironment, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aMaxTasksPerJob, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aTaskTemplate, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aTaskLimit, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aDoScrape, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aExtraAssets, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aAssetScrapers, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aMetadata, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aRetriesWhenFailed, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aRetriesWhenPreempted, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aUseUploadDaemon, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aUploadOnly, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aEmailAddresses, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aDestinationDirectory, cls.aOutput)
        om.MPxNode.attributeAffects(cls.aLocationTag, cls.aOutput)

        om.MPxNode.attributeAffects(cls.aUseCustomRange, cls.aFrameCount)
        om.MPxNode.attributeAffects(cls.aCustomRange, cls.aFrameCount)
        om.MPxNode.attributeAffects(cls.aStartFrame, cls.aFrameCount)
        om.MPxNode.attributeAffects(cls.aEndFrame, cls.aFrameCount)
        om.MPxNode.attributeAffects(cls.aByFrame, cls.aFrameCount)

        om.MPxNode.attributeAffects(cls.aChunkSize, cls.aTaskCount)
        om.MPxNode.attributeAffects(cls.aUseCustomRange, cls.aTaskCount)
        om.MPxNode.attributeAffects(cls.aCustomRange, cls.aTaskCount)
        om.MPxNode.attributeAffects(cls.aStartFrame, cls.aTaskCount)
        om.MPxNode.attributeAffects(cls.aEndFrame, cls.aTaskCount)
        om.MPxNode.attributeAffects(cls.aByFrame, cls.aTaskCount)

        om.MPxNode.attributeAffects(cls.aUseScoutFrames, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aScoutFrames, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aChunkSize, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aUseCustomRange, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aCustomRange, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aStartFrame, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aEndFrame, cls.aScoutTaskCount)
        om.MPxNode.attributeAffects(cls.aByFrame, cls.aScoutTaskCount)

        om.MPxNode.attributeAffects(cls.aUseScoutFrames, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aScoutFrames, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aChunkSize, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aUseCustomRange, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aCustomRange, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aStartFrame, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aEndFrame, cls.aFrameSpec)
        om.MPxNode.attributeAffects(cls.aByFrame, cls.aFrameSpec)

    def compute(self, plug, data):
        """Compute output json from input attribs."""

        print "----------------  IN COMPUTE: ", plug.name()

        if (not ((plug == self.aOutput) or
                 (plug == self.aFrameCount) or
                 (plug == self.aTaskCount) or
                 (plug == self.aScoutTaskCount) or
                 (plug == self.aFrameSpec)
                 )):
            return None

        try:
            sequence = self.get_sequence(data)
        except (ValueError, TypeError):
            pm.displayWarning("Invalid frame sequence specified")
            return None

        scout_sequence = self.get_scout_sequence(data)
        frame_count = len(sequence)
        task_count = sequence.chunk_count()

        scout_task_count = 0
        scout_tasks_sequence = None
        if scout_sequence:
            scout_chunks = sequence.intersecting_chunks(scout_sequence)
            if scout_chunks:
                scout_tasks_sequence = Sequence.create(
                    ",".join(str(chunk) for chunk in scout_chunks))
                scout_task_count = len(scout_chunks)

        self.set_frame_info_plugs(
            data, frame_count, task_count, scout_task_count)

        self.set_frame_spec(data, sequence, scout_tasks_sequence)

        if (plug != self.aOutput):
            return self

        context = self.get_context(data)
        expander = Expander(**context)

        handle = data.outputValue(self.aOutput)
        result = {}
        result.update(self.get_software_environment(data))
        result.update(self.get_instance_type(data))
        result.update(self.get_title(data, expander))
        result.update(self.get_project(data))
        result.update(self.get_tasks(data, sequence, context))
        result.update(self.get_upload_paths(data))
        result.update(self.get_upload_flags(data))
        result.update(self.get_retry_policy(data))
        result.update(self.get_notifiations(data))
        result.update(self.get_scout_frames(scout_sequence))
        result.update(self.get_metadata(data, expander))
        result.update(self.get_location_tag(data))
        result.update(self.get_destination_directory(data))

        handle.setString(json.dumps(result))
        # handle.setString(json.dumps(result, sort_keys=True, indent=4))

        data.setClean(plug)
        return self

    ##############################################################
    @classmethod
    def get_sequence(cls, data):
        chunk_size = data.inputValue(cls.aChunkSize).asInt()
        use_custom_range = data.inputValue(cls.aUseCustomRange).asBool()
        if use_custom_range:
            custom_range = data.inputValue(cls.aCustomRange).asString()
            return Sequence.create(custom_range, chunk_size=chunk_size)

        start_frame = data.inputValue(
            cls.aStartFrame).asTime().asUnits(om.MTime.uiUnit())
        end_frame = data.inputValue(
            cls.aEndFrame).asTime().asUnits(om.MTime.uiUnit())
        by_frame = data.inputValue(cls.aByFrame).asInt()
        return Sequence.create(int(start_frame), int(end_frame), by_frame, chunk_size=chunk_size, chunk_strategy="progressions")

    @classmethod
    def get_scout_sequence(cls, data):
        use_scout_frames = data.inputValue(cls.aUseScoutFrames).asBool()
        if not use_scout_frames:
            return

        scout_frames = data.inputValue(cls.aScoutFrames).asString()
        try:
            return Sequence.create(scout_frames)
        except (ValueError, TypeError):
            return

    @classmethod
    def get_scout_frames(cls, scout_sequence):
        return {"scout_frames": ",".join([str(s) for s in scout_sequence or []])}

    @classmethod
    def set_frame_info_plugs(cls, data, frame_count, task_count, scout_task_count):
        handle = data.outputValue(cls.aFrameCount)
        handle.setInt(frame_count)
        handle.setClean()
        handle = data.outputValue(cls.aTaskCount)
        handle.setInt(task_count)
        handle.setClean()
        handle = data.outputValue(cls.aScoutTaskCount)
        handle.setInt(scout_task_count)
        handle.setClean()

    @classmethod
    def set_frame_spec(cls, data, sequence, scout_sequence):
        handle = data.outputValue(cls.aFrameSpec)
        if scout_sequence:
            result = "{} / {}".format(str(scout_sequence), str(sequence))
        else:
            result = "- / {}".format(str(sequence))

        handle.setString(result)
        handle.setClean()

    @classmethod
    def get_instance_type(cls, data):
        return {
            "instance_type": data.inputValue(cls.aInstanceTypeName).asString(),
            "preemptible": data.inputValue(cls.aPreemptible).asBool()
        }

    @classmethod
    def get_title(cls, data, expander):
        title = data.inputValue(cls.aTitle).asString()
        return {"job_title": expander.evaluate(title)}

    @classmethod
    def get_project(cls, data):
        return {"project": data.inputValue(cls.aProjectName).asString()}

    @classmethod
    def get_software_environment(cls, data):
        extra_env = cls.get_extra_env(data)
        packages_data = cls.get_software_packages(data)
        packages_data["env"].extend(extra_env)
        return {
            "environment": dict(packages_data["env"]),
            "software_package_ids": packages_data["ids"]
        }

    @classmethod
    def get_software_packages(cls, data):
        tree_data = software.data()
        paths = []
        host_path = data.inputValue(cls.aHostSoftware).asString()
        paths.append(host_path)
        array_handle = data.inputArrayValue(cls.aPluginSoftware)

        while not array_handle.isDone():
            plugin_path = "{}/{}".format(host_path,
                                         array_handle.inputValue().asString())
            paths.append(plugin_path)
            array_handle.next()

        result = {
            "ids": [],
            "env": PackageEnvironment()

        }

        for package in filter(None, [tree_data.find_by_path(path) for path in paths if path]):
            if package:
                result["ids"].append(package["package_id"])
                result["env"].extend(package)

        return result

    @classmethod
    def get_extra_env(cls, data):
        result = []
        array_handle = data.inputArrayValue(cls.aExtraEnvironment)
        while not array_handle.isDone():
            name = array_handle.inputValue().child(
                cls.aExtraEnvironmentKey).asString()
            value = array_handle.inputValue().child(
                cls.aExtraEnvironmentValue).asString()
            exclusive = array_handle.inputValue().child(
                cls.aExtraEnvironmentExclusive).asBool()
            name = name.strip()
            value = value.strip()

            if name and value:
                result.append(
                    {
                        "name": name,
                        "value": value,
                        "merge_policy": "exclusive" if exclusive else "append"
                    }
                )
            array_handle.next()
        return result

    def get_context(self, data):
        node = om.MFnDependencyNode(self.thisMObject())
        current_layer = pm.editRenderLayerGlobals(
            query=True, currentRenderLayer=True)
        file_name = pm.sceneName()
        scene_name = os.path.splitext(os.path.split(file_name)[1])[0]

        context = {
            "Scene": scene_name,
            "SceneFile": file_name,
            "Object": node.name(),
            "RenderLayer": layer_utils.get_layer_name(current_layer),
            "WorkspacePath": pm.workspace(query=True, rd=True),
            "OutputPath":  data.inputValue(self.aDestinationDirectory).asString().strip(),
            "Renderer": pm.PyNode("defaultRenderGlobals").attr("currentRenderer").get(),
            "ConductorVersion": pm.moduleInfo(version=True, moduleName="conductor")
        }

        low_context = {}
        for key in context:
            key_lower = key.lower()
            if not key_lower in context:
                low_context[key_lower] = context[key]
        context.update(low_context)
        return context

    @classmethod
    def get_tasks(cls, data, sequence, context):
        if data.inputValue(cls.aUploadOnly).asBool():
            return {}

        tasks = []
        template = data.inputValue(cls.aTaskTemplate).asString()
        limit = data.inputValue(cls.aTaskLimit).asInt()
        chunks = sequence.chunks()
        if limit < 0:
            limit = len(chunks)
        for i, chunk in enumerate(chunks):
            if i >= limit:
                break
            task_context = {
                "start": str(chunk.start),
                "end": str(chunk.end),
                "step": str(chunk.step),
                "chunk_length":  str(len(chunk))
            }
            task_context.update(context)
            expander = Expander(**task_context)

            tasks.append({
                "command": expander.evaluate(template),
                "frames": str(chunk)
            })
        return {"tasks_data": tasks}

    @classmethod
    def get_upload_flags(cls, data):
        return {
            "upload_only": data.inputValue(cls.aUploadOnly).asBool(),
            "local_upload": not data.inputValue(cls.aUseUploadDaemon).asBool()
        }

    @classmethod
    def get_retry_policy(cls, data):
        return {
            "autoretry_policy": {
                "preempted": {"max_retries":  data.inputValue(cls.aRetriesWhenPreempted).asInt()},
                "failed":    {"max_retries":   data.inputValue(cls.aRetriesWhenFailed).asInt()}
            }
        }

    @classmethod
    def get_notifiations(cls, data):
        result = []
        array_handle = data.inputArrayValue(cls.aEmailAddresses)
        while not array_handle.isDone():
            if array_handle.inputValue().child(
                    cls.aEmailAddressActive).asBool():
                value = array_handle.inputValue().child(
                    cls.aEmailAddress).asString().strip()
            if value:
                result.append(value)
            array_handle.next()
        return {"notify": result}

    @classmethod
    def get_upload_paths(cls, data):
        path_list = PathList()
        path_list.add(*cls.get_scraped_paths(data))
        path_list.add(*cls.get_cached_paths(data))
        path_list.glob()
        return {"upload_paths": sorted([p.posix_path() for p in path_list])}

    @classmethod
    def get_scraped_paths(cls, data):
        result = []
        if not data.inputValue(cls.aDoScrape).asBool():
            return result
        array_handle = data.inputArrayValue(cls.aAssetScrapers)
        while not array_handle.isDone():
            if array_handle.inputValue().child(cls.aAssetScraperActive).asBool():
                script_path = array_handle.inputValue().child(cls.aAssetScraperPath).asString()
                try:
                    mod_name = "conductor.maya.{}".format(
                        os.path.splitext(os.path.basename(script_path))[0])
                    scraper_module = imp.load_source(mod_name, script_path)
                except IOError:
                    pm.warning(
                        "Can't load the script '{}' as a Python module.".format(script_path))
                    raise
                except SyntaxError:
                    pm.warning(
                        "Syntax error in the scraper script: '{}'.".format(script_path))
                    raise
                result += scraper_module.run()
            array_handle.next()

        return [p["path"] for p in result]

    @classmethod
    def get_cached_paths(cls, data):
        result = []
        array_handle = data.inputArrayValue(cls.aExtraAssets)
        while not array_handle.isDone():
            path = array_handle.inputValue().asString().strip()
            if path:
                result.append(path)
            array_handle.next()
        return result
 

    @classmethod
    def get_metadata(cls, data, expander):
        metadata = {}
        array_handle = data.inputArrayValue(cls.aMetadata)
        while not array_handle.isDone():
            key = array_handle.inputValue().child(
                cls.aMetadataKey).asString().strip()
            value = array_handle.inputValue().child(
                cls.aMetadataValue).asString().strip()

            metadata[key] = value

            array_handle.next()

        return {"metadata": expander.evaluate(metadata)}

    @classmethod
    def get_location_tag(cls, data):
        return {"location": data.inputValue(cls.aLocationTag).asString().strip()}

    @classmethod
    def get_destination_directory(cls, data):
        return {"output_path": data.inputValue(cls.aDestinationDirectory).asString().strip()}
