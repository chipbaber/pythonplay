### Quick Reference to Install Python SDK on Windows with OCI Python SDK
Want to get started developing against the Oracle Cloud Infrastructure (OCI) with those python coding skills you picked up? This video shows how to go from zero to executing your first python script on Windows. It is designed for those developers who don't want to wade through documentation, just want to dive in and get started. Lets get started. 

- Open Powershell on your PC. 
![](assets/2024-05-16-09-09-22.png)

- Issue the following command in powershell to get the version of Windows you are running.
```
slmgr /dlv
``` 
![](assets/2024-05-16-09-16-07.png)

- Check to see if python is installed already. 
```
python --version
```

if installed you will see something like this showcasing the version installed as well.  
![](assets/2024-05-16-09-13-20.png)

if not installed 

- Navigate to the following link to see the supported versions of python for the OCI python SDK for your Windows OS version. [https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm#Requirements__SupportedPythonVersionsandOperatingSystems](Supported Python Versions for SDK by OS)


- Install a supported version of Python. [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

- Test python install in powershell.
```
python --version
```

- Check to pip install version. 
```
pip --version
```

- If older version you may want to upgrade. 
```
python.exe -m pip install --upgrade pip
```

- Issue the following command to install python sdk. 
```
pip install oci
```

- Create a .oci directory to house your config file. For example C:\Users\CBABER\ would be a user homepath. Launch notepad to create the .oci config, if you have multiple tenancies I would suggest adding a .<tenancyname> at the end. 
```
mkdir C:\Users\CBABER\.oci
cd C:\Users\CBABER\.oci
notepad config.chipspicks
```

- Navigate to your identity on OCI. If a fingerprint exists you can leverage it. Otherwise you will need to create a new one. Once created you can copy over the information required for your config file. 


- Test your install by placing the code below in a new file called listCompartments.py.
```
import oci
print("Starting Program");
from oci.config import from_file
# Config file is read from user's home location i.e., ~/.oci/config
config = from_file(file_location=".oci/config.chipspicks")  
# root compartment OCID
COMPARTMENT_ID="<add root compartment id>" 
print(COMPARTMENT_ID);
identity_client = oci.identity.IdentityClient(config)
list_compartments_response = identity_client.list_compartments(compartment_id=COMPARTMENT_ID,compartment_id_in_subtree=True)
# Get the list of compartments including child compartments except root compartment
compartmentlist = list_compartments_response.data
# Get the details of root compartment & append to the compartment list so that we have the full list of compartments in the given tenancy
root_compartment = identity_client.get_compartment(
    compartment_id=COMPARTMENT_ID).data
compartmentlist.append(root_compartment)
print(compartmentlist);
```

- Execute your example python script. 
```
python listCompartments.py
```


- If you want to remove the OCI Python SDK issue the following command. 
```
pip uninstall oci
```
![](assets/2024-05-16-09-22-47.png)


- Test Command for show all 
```
python showoci.py -c -d -csv  C:\temp\output -cf C:\Users\CBABER\.oci\config
```