# Overview

The purpose of this hook is to enable and disable
[stack termination protection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html).

A common use case is execute this hook with your CI/CD
system. In that case you may need to execute this on every
change.  That's where the
[sceptre-date-resolver](https://github.com/sceptre/sceptre-date-resolver)
may help. It will allow you to force AWS cloudformation to execute the
template on on every commit.


## Available Hooks

### StackTermination

Enables and disables cloudformation stack termination.

Syntax:

```yaml
parameter|sceptre_user_data:
    <name>: !stack_termination_protection <setting>
```
Valid setting:
* enabled
* disabled


Example:

Enable stack termination protection after creating stack
and disable stack termination protection before stack deletion:
```
hooks:
  after_create:
    - !stack_termination_protection 'enabled'
  before_delete:
    - !stack_termination_protection 'disabled'
```
