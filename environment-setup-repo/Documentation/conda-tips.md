# Working With Conda Environments

## Importing Environments

To make sure everyone is working in the same development environment, we are using Conda to manage our Python environments.

The easiest way to pass environment imfo from one machine to anohter is to use a YAML file to list out the environment dependencies. This YAML file can be imported into Anaconda Navigator or through the command line to create a new environment on your machine.

### Importing with Anaconda Navigator
1. Open Anaconda Navigator and go to the Environments tab
2. At the bottom of the environments pane, click "Import"
3. Set a name for the environment
4. Use the file updload wizard to select the environment.yaml file

### Importing with Command Line
1. Navigate to the same directory as the `environment.yaml` file 
2. Run the following command:

    `conda env create -f environment.yaml`


## Updating Environments

You can update an existing environment from a YAML file through the command line. That way you can update your environment's YAML file and you dont need to delete and re-create the environment every time you add or remove a dependency. 

1. Navigate to the same directory as the `environment.yaml` file 
2. Set the environment you want to update as the active environment:
    
    `conda activate [ENVIRONMENT_NAME]`

3. Update the active environment:

    `conda env update -f environment.yaml`

4. Optional: deactivate the currently active environment

    `conda deactivate`


## Exporting Environments

When creating an environment from scratch, we used Anaconda Navigator to create the environment on our local machine, then exported the YAML for that environment so that it could be shared.

**Important:**

The YAML produced by default is not compatible between Windows and MacOS, so you need to modify it before it can be shared.

Also, the default YAML has a lot of extra stuff in it that can be removed to make the file easier to read. 

### Generating the Environment YAML File
1. Navigate to the directory you want to create the file in 
2. Set the environment you want to export as the active environment:
    
    `conda activate [ENVIRONMENT_NAME]`

3. Export the active environment:

    `conda env export > environment.yaml`

### Clean Up the Generated Environment YAML

The generated YAML has way more information that you need in it. 

Keep the following properties and get rid of everything else:

- "name"
- "dependencies"

For the dependencies, you only need to keep the really important modules in the list. All of the dependency libraries and modules will be installed automatically so you dont need to specify them. 

Also, the module definition can be simplified to only include the module name and the version number. Version number is optional, but we decided to keep it so that we can keep all environments identical.

### Cleaned up example

Here is an example of what a cleaned up YAML file would look like:

```yaml
name: environment-name
dependencies:
    - keras-applications=1.0.8
    - keras-preprocessing=1.1.0
    - markdown=3.1.1
    - notebook=6.0.1
    - pandas=0.25.2
    - pip=19.3.1
    - python=3.6.9
    - scipy=1.3.1
    - tensorflow=2.0.0
    - matplotlib=3.1.1
```



## Helpful Conda Commands

| Function                  | Command                                   |
| :---                      |     ----:                                 |
| List Environments         | `conda info -e`                           |
| Activate Environment      | `conda activate [ENV_NAME]`               |
| Deactivate Environment    | `conda deactivate`                        |
| Create Environment        | `conda env create -f environment.yaml`    |
| Update Environment        | `conda env update -f environment.yaml`    |
| Export Environment        | `conda env export > environment.yaml`     |
