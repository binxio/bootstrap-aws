#!env python

import yaml


class AWSBootstrap(object):

    def __init__(self, verbose=False):
        self.aws_credentials = '~/.aws/credentials'
        self.aws_config = '~/.aws/config'
        self.bootstrap_temp = './temp_file.yml'
        self.bootstrap = None
        self.role_access_keys = None
        self.personal_access_keys = None

    def get_profile(self):
        """ get the access keys from the provided profile """
        """ set them as personal_access_keys """

    def assume_role(self, account_id, role):
        """ ask user for token """
        """ assume role """
        """ build retry in case of error """
        return access_keys

    def deploy_cfn_stack(self, account, stack):
        account_id = get_account_id(account['Name'])
        """ assume_role """
        """ init cfn client """
        """ check if stack is deployed, save output values """
        """ deploy or update the stack """
        """ pause loop until deployment is finished """
        """ refresh_bootstrap_yml() """

    def create_organisation(self, account):
        set_aws_client('organisations', self.role_access_keys)
        """ get organisation (check if already deployed """
        """ looppause when still creating (in case script was aborted) """
        """ when verbose: list the organisation and the status """
        """ create new, pause when it's creating """

        output_dict = response['Output']
        reserved = {'AccountId': account_id}
        setattr(self.accounts, account_name, {**output_dict, **reserved})

    def refresh_bootstrap_yml(self):
        """ After each stack deploy, refresh to write the files """
        replace = {
            "${Accounts.Management.AccountId}": "123456789"
            "${Accounts.Production.AccountId}": "324342342"
        }
        """ replace strings, write result to self.bootstrap_temp_file """
        with open(self.bootstrap_temp_file, 'r') as stream:
            try:
                self.bootstrap = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def set_aws_client(self, aws_client, access_keys):
        """
        Initiates the aws client, for iam, sts and cloudformation for example
        """
        """ check if current client == aws_client and not expired """
        kwargs = {
            'aws_access_key_id': access_keys['aws_access_key_id'],
            'aws_secret_access_key': access_keys['aws_secret_access_key']
        }
        if 'aws_session_token' in access_keys:
            kwargs['aws_session_token'] = access_keys['aws_session_token']

        setattr(self, aws_client, boto3.client(aws_client, **kwargs))

    def main(self):
        """
        Creats organisations and deploys stacks.
        """
        refresh_bootstrap_yml()

        for account in self.bootstrap[Accounts]:
            create_organisation(account)

        for account in self.bootstrap[Accounts]:
            for stack in account.stacks:
                deploy_cfn_stack(stack)
