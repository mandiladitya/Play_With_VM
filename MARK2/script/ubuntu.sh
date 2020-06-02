a=`sudo docker run -d -P eg_sshd` 
b=`sudo docker port $a | tail -c 6`

echo  "ssh root@ec2-18-218-253-210.us-east-2.compute.amazonaws.com -p $b"   
