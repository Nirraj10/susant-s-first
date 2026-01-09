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

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
  Name = "my-frist-igw"
  ManagedBy = "Terraform"
  Project = "network_vpc"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws.vpc.main.vpc_id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

resource "aws_route-table-association" "public" {
  subnet_id = aws_subnet.public.id
  route_table_id = aws_route-table.public.id
}