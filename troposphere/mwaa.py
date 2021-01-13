from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ModuleLoggingConfiguration(AWSProperty):

    props = {
        "CloudWatchLogGroupArn": (basestring, False),
        "Enabled": (boolean, False),
        "LogLevel": (basestring, False)
    }


class LoggingConfiguration(AWSProperty):

    props = {
        "DagProcessingLogs": ModuleLoggingConfiguration,
        "SchedulerLogs": ModuleLoggingConfiguration,
        "TaskLogs": ModuleLoggingConfiguration,
        "WebserverLogs": ModuleLoggingConfiguration,
        "WorkerLogs": ModuleLoggingConfiguration
    }


class SecurityGroupList(AWSProperty):

    props = {
        "SecurityGroupList": ([basestring], False)
    }


class SubnetList(AWSProperty):

    props = {
        "SubnetList": ([basestring], False)
    }


class NetworkConfiguration(AWSProperty):

    props = {
        "SecurityGroupIds": SecurityGroupList,
        "SubnetIds": SubnetList
    }


class Environment(AWSObject):
    resource_type = "AWS::MWAA::Environment"

    props = {
        'Name': (basestring, True),
        # 'AirflowConfigurationOptions': (AirflowConfigurationOptions, False),
        'AirflowVersion': (basestring, False),
        'DagS3Path': (basestring, False),
        'EnvironmentClass': (basestring, False),
        'ExecutionRoleArn': (basestring, False),
        'KmsKey': (basestring, False),
        'LoggingConfiguration': (LoggingConfiguration, False),
        'MaxWorkers': (integer, False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'PluginsS3ObjectVersion': (basestring, False),
        'PluginsS3Path': (basestring, False),
        'RequirementsS3ObjectVersion': (basestring, False),
        'RequirementsS3Path': (basestring, False),
        'SourceBucketArn': (basestring, False),
        'Tags': (Tags, False),
        'WebserverAccessMode': (basestring, False),
        'WebserverUrl': (basestring, False),
        'WeeklyMaintenanceWindowStart': (basestring, False)
    }
