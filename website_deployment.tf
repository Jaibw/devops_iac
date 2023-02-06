provider "aws" {
	region     = "ap-northeast-1"
}

resource "aws_instance" "website01" {
	ami = "ami-0cd7ad8676931d727"
	instance_type = "t2.micro"
	associate_public_ip_address = "true"
	key_name = "AWS-KEY"
	user_data = <<EOF
#! /bin/bash
sudo apt-get update
sudo apt-get install -y nginx
sudo apt-get install -y git 
sudo rm -vrf /var/www/html
sudo git clone https://github.com/Jaibw/FrozenYogurtShop.git /var/www/html
sudo systemctl start nginx
sudo systemctl enable nginx
	EOF
	tags = {
		Name = "INSTANCE-NAME"
	}
}
