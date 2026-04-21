import subprocess

def terraform_run(command):
    subprocess.run(command, shell=True, check=True)
    # print(process.stdout.decode())

# directory = '/mnt/d/DevOps/Python/project/terraform-automate/Wanderlust-Mega-Project-main/terraform'
directory = 'D:/DevOps/Python/project/terraform-automate/Wanderlust-Mega-Project-main/terraform'
# command = f'terraform -chdir={directory} init'
# command = f'terraform -chdir={directory} plan'
command = f'terraform -chdir={directory} apply -auto-approve'
command = f'terraform -chdir={directory} destroy -auto-approve'

# print(command)
terraform_run(command)