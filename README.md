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


### Use Case 3: Manage users, cloud accounts, account groups, policies and alert rules

1.  Using the Terraform provider, you can perform CRUD operations on the
    following Prisma objects: Users, Cloud Accounts, Policies, Alert
    Rules and also READ operations on Alerts.
