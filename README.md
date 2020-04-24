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

### Use Case 2: On-boarding AWS Orgs

1.  Prepare the AWS accounts by creating the Prisma cloud role in your AWS
    Master account and all the member accounts. With the recent announcement of
    AWS Cloudformation
    [stacksets](https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/),
    you can now simplify the configuration of cross-accounts IAM
    permissions and allow for automatic creation and deletion of
    resources when AWS accounts are joining or are removed from AWS
    Organization.
2.  Follow the instructions from the AWS Stack Set documentation here to
    [set up roles in the child
    accounts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)
    that have permissions to deploy resources with a trust relationship
    that maps to the role of the parent account from which you're deploying from.
3.  Create a StackSet in the Master account and deploy a Cloudformation
    template into selected accounts or Organizational Units (OU).
4.  Download the CSV file template from: [CSV Template for AWS Account On-boarding - Sheet1.csv](https://github.com/PaloAltoNetworks/PrismaCloud_TF_BulkOnboarding_and_AWS_Orgs/blob/master/CSV%20Template%20for%20AWS%20Account%20On-boarding%20-%20Sheet1.csv)
5.  Populate the CSV with the required fields (eg. AWS account numbers,
    external ID and Prisma cloud role ARN)
6.  Invoke the Terraform Provider in your terraform scripts.
7.  Whenever new AWS account is added/deleted, please update the CSV file and re-trigger the terraform script

### Use Case 3: Manage users, cloud accounts, account groups, policies and alert rules

1.  Using the Terraform provider, you can perform CRUD operations on the
    following Prisma objects: Users, Cloud Accounts, Policies, Alert
    Rules and also READ operations on Alerts.
