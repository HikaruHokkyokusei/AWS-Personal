# Notes:

## 1. Setting Webhooks for CodeBuild

Presently, AWS does not allow to set webhooks for GitHub Enterprise Projects using `Cloud Formation Template`.
For standard scenarios, the code would have been: -

```json
{
    "...": {},
    "Resources": {
        "...": {},
        "CodeBuild": {
            "Type": "WS::CodeBuild::Project",
            "Properties": {
                "...": {},
                "Triggers": {
                    "Webhook": true,
                    "FilterGroups": [
                        [
                            {
                                "Type": "EVENT",
                                "Pattern": "PUSH"
                            },
                            {
                                "Type": "BASE_REF",
                                "Pattern": "^refs/heads/master$",
                                "ExcludeMatchedPattern": false
                            }
                        ]
                    ]
                }
            }
        }
    }
}
```

But in case of GitHub Enterprise project, we need to set this webhook from the AWS CLI.
This is done under `Source` under `Primary source webhook events` when creating or updating a Code Build Project.