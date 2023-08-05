# -*- coding: utf-8 -*-

import abc
import six
import logging

from botocore.exceptions import ClientError

from sceptre.hooks import Hook


@six.add_metaclass(abc.ABCMeta)
class StackTerminationProtection(Hook):
    """
    Hook for cloudformation stack protection.

    :param argument: The stack termination protection setting
    :type argument: str

    """
    ALLOWED_ARG_VALUES = ['enabled', 'disabled']

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        super(StackTerminationProtection, self).__init__(*args, **kwargs)

    def run(self):
        """
        Updates the cloudformation stack termination protection setting

        :returns: parameter value
        :rtype: str
        """
        if not self.argument:
            return

        argument = (self.argument if self.argument else '').lower()
        assert argument in self.ALLOWED_ARG_VALUES, \
            "Invalid argument for !stack_termination_protection, " \
            "please choose one of {0}".format(self.ALLOWED_ARG_VALUES)

        enable_termination_protection = False
        if argument == 'enabled':
            enable_termination_protection = True
        connection_manager = self.stack.connection_manager
        try:
            connection_manager.call(
                service="cloudformation",
                command="describe_stacks",
                kwargs={"StackName": self.stack.external_name}
            )
        except ClientError:
            self.logger.info(
                "%s - stack not found. Skipping termination protection",
                self.stack.name)
            return
        try:
            connection_manager.call(
                service="cloudformation",
                command="update_termination_protection",
                kwargs={"StackName": self.stack.external_name,
                        "EnableTerminationProtection":
                            enable_termination_protection},
                profile=self.stack.profile,
                region=self.stack.region,
                stack_name=self.stack.name
            )
            self.logger.info(
                "%s - termination protection set to '%s'",
                self.stack.name, argument)
        except ClientError as e:
            raise e
