# Conductor-Maya

Conductor-Maya is Maya plugin that contains a Submitter for the Conductor Cloud rendering service.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Conductor-Maya. 

```bash
pip install conductor.maya 
```
You can install conductor.maya either globally or in a [virtual environment](https://virtualenv.pypa.io/en/latest/). In either case, after installation, you'll need to create a module file to let Maya know where it is installed. 

Run the following script to automatically create a Maya module file.

```bash
setup_maya
```

## Usage

The plugin provides a **conductorRender** node to submit rendering jobs based on values in Maya's **RenderSettings** node.

#### To set up a render:
* Open a scene that's ready to render.
* Use the Plugin Manager to load the Conductor plugin. A Conductor Menu will appear in the main menu bar.
* Choose **Conductor->Submitter->Create**.
* In the attribute editor, press **Connect to Conductor** and sign in if necessary.
* Choose an instance type and set up other parameters as required.
* Press submit.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[BSD 3 Clause](https://choosealicense.com/licenses/bsd-3-clause-clear/)