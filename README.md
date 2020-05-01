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

### Use Case 1: Bulk on-boarding of cloud accounts (AWS)

1.  Prepare the AWS accounts by creating the Prisma cloud role in all of
    your accounts.

2.  You can use one of following two methods to create the Prisma cloud
    role in AWS accounts:

    a.  Using Terraform -
        > [*https://github.com/wwce/terraform/tree/master/aws/RedLock-IAMroles-tf*](https://github.com/wwce/terraform/tree/master/aws/RedLock-IAMroles-tf)

    b.  Using Cloud Formation -
        > [*https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/connect-your-cloud-platform-to-prisma-cloud/onboard-your-aws-account/set-up-your-prisma-cloud-role-for-aws-manual.html\#ide7b46e67-8e1f-400f-b763-48bbe41bbe2c*](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/connect-your-cloud-platform-to-prisma-cloud/onboard-your-aws-account/set-up-your-prisma-cloud-role-for-aws-manual.html#ide7b46e67-8e1f-400f-b763-48bbe41bbe2c)

3.  Download the CSV file template from: [CSV Template for AWS Account On-boarding - Sheet1.csv](https://github.com/PaloAltoNetworks/PrismaCloud_TF_BulkOnboarding_and_AWS_Orgs/blob/master/CSV%20Template%20for%20AWS%20Account%20On-boarding%20-%20Sheet1.csv)

4.  Populate the CSV with the required fields (eg. AWS account numbers,
    external ID and Prisma cloud role ARN)

5.  Invoke the Terraform Provider in your terraform scripts.

6.  If you add a new AWS account, please update the CSV file and re-run Terraform.



### Use Case 3: Manage users, cloud accounts, account groups, policies and alert rules

1.  Using the Terraform provider, you can perform CRUD operations on the
    following Prisma objects: Users, Cloud Accounts, Policies, Alert
    Rules and also READ operations on Alerts.
