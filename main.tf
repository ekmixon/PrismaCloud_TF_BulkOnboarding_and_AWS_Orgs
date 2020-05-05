# Configure the prismacloud provider

provider "prismacloud" {
    json_config_file = ".prismacloud_auth.json"
}

locals {
    instances = csvdecode(file("awsaccountsfile.csv"))
}

// Now specify the cloud account resource with a loop like so:
resource "prismacloud_cloud_account" "csv" {
    for_each = { for inst in local.instances : inst.name => inst }

    aws {
        name = each.value.name
        account_id = each.value.accountId
        external_id = each.value.externalId
        group_ids = split("||", each.value.groupIDs)
        role_arn = each.value.roleArn
    }
}
