variable "aws_region" {
  description = "AWS region where resources will be provisioned"
  default     = "us-east-2"
}

variable "ami_id" {
  description = "AMI ID for th  e EC2 instance"
  default     = "ami-0a1b6a02658659c2a"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  default     = "t3.micro"
}
