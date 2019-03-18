import boto3
import os
import shutil
import sys

if __name__ == "__main__":

    print(len(sys.argv))
    if len(sys.argv)==4:
        sourceFile=sys.argv[1]
        destdirroot=sys.argv[2]
        socialmedia=sys.argv[3]
    else:
        print('wrong number of argument')
        exit(-1)
    #shutil.rmtree('/Users/anshu/Documents/sih/linkedin/Data/.DS_Store')
    print(destdirroot+socialmedia+"_response.txt");
    input = open(destdirroot+socialmedia+"_response.txt",'r')
    content = input.readlines()
    urls = [url.strip() for url in content]
    input.close()

    if(len(urls) > 0):
        #urls = urls[:1]

        client = boto3.client('rekognition')
        res = open(destdirroot+"result.txt",'w')
        found = False

        if (socialmedia == "linkedin"):
            destdir = destdirroot+"Data/"+"test/"
        else:
            destdir = destdirroot+"Data/"

        print(destdir)
        destfolders = os.listdir(destdir)
        print(destfolders)
        if(len(destfolders) > 1 and socialmedia=="linkedin" ):
            if(".DS_Store" in destfolders):
                destfolders.remove(".DS_Store")
        print(destfolders)
        # destfiles = sorted(destfiles, key = lambda x: x.split('.')[0])

        confidence_max=69.0
        for i in range(0,len(destfolders)):
            comparison_condition=destdir + destfolders[i]
            if(socialmedia == "linkedin"):
                comparison_condition=destdir
            if(len(os.listdir(comparison_condition)) > 0):
                if(socialmedia == "linkedin"):
                    cd = destdir
                else:
                    cd = destdir + destfolders[i] + '/Uploaded Photos/'
                os.chdir(cd)
                destfiles = os.listdir(cd)
                for j in range(0,len(destfiles)):

                    targetFile = cd + destfiles[j]
                    print('Scanning : ' + targetFile)
                    imageSource = open(sourceFile,'rb')
                    imageTarget = open(targetFile,'rb')

                    try:
                        response = client.compare_faces(SimilarityThreshold = 70, SourceImage = {'Bytes': imageSource.read()}, TargetImage = {'Bytes': imageTarget.read()})

                        for faceMatch in response['FaceMatches']:
                            position = faceMatch['Face']['BoundingBox']
                            similarity = faceMatch['Similarity']
                            # print(str(i+1) + ' The faces at ' + str(position['Left']) + ' and ' + str(position['Top']) + ' match with ' + similarity + '% confidence')
                            if(similarity > confidence_max):
                                if(socialmedia == "facebook"):
                                    confidence_max = similarity
                                    user=targetFile.split('/')
                                    username=user[7]
                                else:
                                    confidence_max = similarity
                                    user=targetFile.split('/')[-1]
                                    username=int(user[3:len(user)-4])
                        imageSource.close()
                        imageTarget.close()
                    except:
                        imageSource.close()
                        imageTarget.close()
                        continue
            imageSource.close()
            imageTarget.close()

        if(socialmedia == "facebook"):
            if(confidence_max > 69.0):
                res.write('Found a match with ' + str(confidence_max) + '% confidence !  :  ' + username + '\n')
            else:
                res.write('Sorry, No match found !')
        else:
            if(confidence_max > 69.0):
                res.write('Found a match with ' + str(confidence_max) + '% confidence !  :  ' + urls[username] + '\n')
            else:
                res.write('Sorry, No match found !')

        res.close()
        # os.remove(sourceFile)
        shutil.rmtree(destdir)
        # os.makedirs(destdir)
        print('Done !! Checkout result.txt')
    else:
        print('Exiting...')