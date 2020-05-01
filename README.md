# Terraform Provider for Prisma Cloud - Alpha Version

Prisma Cloud has developed a Terraform provider for Prisma Cloud. You
can use this provider for the following use cases:

1.  Bulk, automated on-boarding of cloud accounts (AWS, Azure, GCP) into
    Prisma Cloud
2.  On-boarding of cloud accounts from AWS Organizations.
3.  Managing users, cloud accounts, account groups, policies and alert
    rules in an automated way using Terraform. This enables you to
    manage Prisma Cloud as Infrastructure-as-code (IaC).

The following sections provide step-by-step instructions for the above
use cases.

## Pre-requisites:

1.  Download the latest version of Prisma Cloud Terraform provider from
    the following GitHub repository.

    a.  [*https://github.com/PaloAltoNetworks/terraform-provider-prismacloud*](https://github.com/PaloAltoNetworks/terraform-provider-prismacloud)

    b.  Note: The documentation on how to build and use the provider is
        included in GitHub repo. The documentation will be made
        available on Terraform website once it goes through the
        certification process.  A good start: [*https://github.com/PaloAltoNetworks/terraform-provider-prismacloud/blob/master/website/docs/r/cloud_account.html.markdown*](https://github.com/PaloAltoNetworks/terraform-provider-prismacloud/blob/master/website/docs/r/cloud_account.html.markdown)

2.  Please refer to Prisma Cloud API located at
    [*https://api.docs.prismacloud.io/reference*](https://api.docs.prismacloud.io/reference)




### Use Case 3: Manage users, cloud accounts, account groups, policies and alert rules

1.  Using the Terraform provider, you can perform CRUD operations on the
    following Prisma objects: Users, Cloud Accounts, Policies, Alert
    Rules and also READ operations on Alerts.
