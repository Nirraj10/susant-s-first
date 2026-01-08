resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "susant-vpc"
    ManagedBy = "Terraform"
    Project = "network_vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id = aws.vpc.main.vpc_id
  cidr_block = "10.0.0.0/24"

    tags = {
    Name = "susant-vpc"
    ManagedBy = "Terraform"
    Project = "network_vpc"
  }
}