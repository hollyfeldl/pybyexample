# the defer example usling finally of a try block

def main():

    try:
        print("creating")
        theFile = open("/tmp/defer.txt" ,"w")
        print("writing")
        theFile.write("data\n")        

    except Exception as e:
        print("The exception:", e)
        raise e
    finally:
        print("closing")
        theFile.close()



if __name__ == "__main__":
    main()