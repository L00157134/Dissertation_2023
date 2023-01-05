from tkinter import *

main = Tk()

def button_clicked():
    text = Label(main, text="Configuration Locked!")
    text.pack()
    import json
    import boto3
  
    s3_client = boto3.client("s3")
  
    bucket_name = "terraform-sate-lock-rosh"
  
    bucket_policy = {
      "Id":
      "sid1",
      "Version":
      "2012-10-17",
      "Statement": [{
          "Sid": "Statelock",
          "Action": ["s3:GetObject", 
                     "s3:DeleteObject"],
          "Effect": "Deny",
          "Resource": ["arn:aws:s3:::terraform-sate-lock-rosh/*"],
          "Principal": "*"
      }]
  }
  
    response = s3_client.put_bucket_policy(Bucket=bucket_name,
                                          Policy=json.dumps(bucket_policy))
  
    print(response)

def button_unclicked():
    text = Label(main, text="Configuration UnLocked!")
    text.pack()
    import boto3
    s3 = boto3.client('s3')
    s3.delete_bucket_policy(Bucket='terraform-sate-lock-rosh')

button_one = Button(main,text="Lock Config", fg="gold", bg="black", command=button_clicked)

button_one.pack()


button_two = Button(main,text="UnLock Config", fg="gold", bg="black", command=button_unclicked)

button_two.pack()

main.mainloop()
