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