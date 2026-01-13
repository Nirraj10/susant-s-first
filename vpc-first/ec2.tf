resource "aws_instance" "web" {
  ami                         = "ami-0b0ea68c435eb488d"
  associate_public_ip_address = true
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [ aws_security_group.public_http_traffic.id ]
  root_block_device {
    delete_on_termination     = true
    volume_size               = 10
    volume_type               = "gp3"
 }
}

resource "aws_security_group" "public_http_traffic" {
  description = "Security group allowing traffic on ports 443 and 80"
  name        = "public-http-traffic"
  vpc_id      = aws_vpc.main.id
}

resource "aws_vpc_security_group_ingress_rule" "http" {
    security_group_id = aws_security_group.public_http_traffic.id
    cidr_ipv4   = "0.0.0.0/0"
    from_port   = 80
    to_port     = 80
    ip_protocol = "tcp"
}

resource "aws_vpc_security_group_ingress_rule" "htpps" {
    security_group_id = aws_security_group.public_http_traffic.id
    cidr_ipv4   = "0.0.0.0/0"
    from_port   = 443
    to_port     = 443
    ip_protocol = "tcp"
}