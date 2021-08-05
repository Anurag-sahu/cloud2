  import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A1-hbmNtCaEOeWrfcnbTqxR17j7iEqcoJRpFIx4f-qP-P0HK8RlT89wTUGyZzBtHDBHZrZnF5sEQ4bkXnEOH4a8AhI98OY8oCaEKqUFG06oMCFgaSwKa87CMp5GeUc407u0pMVw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()