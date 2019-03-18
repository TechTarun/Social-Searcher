import requests
import sys
query_len = len(sys.argv)
query = ''

if(query_len == 1):
    print('Nothing Entered !')
else:
    for i in range(1,query_len):
        query += str(sys.argv[i]) + ' '

print('Query is'+query)

def apicall(query,key):
    if(key == '27b93395fdf9dafb0e3ab2610456b66f'):
        response = requests.get('https://api.social-searcher.com/v2/search?q='+query+'&lang=en&limit=100&key=27b93395fdf9dafb0e3ab2610456b66f')
        data = response.json()
        print(data)
        if(data['meta']['http_code'] == 403):
            return apicall(query,'6af9f471206608881d0ee3b76ca171d1')
        return data
    elif(key == '6af9f471206608881d0ee3b76ca171d1'):
        response = requests.get('https://api.social-searcher.com/v2/search?q='+query+'&lang=en&limit=100&key=6af9f471206608881d0ee3b76ca171d1')
        data = response.json()
        return data

data = apicall(query,'27b93395fdf9dafb0e3ab2610456b66f')
print('Done calling API...')

fb = open('/Users/anshu/Documents/sih/facebook/facebook_response.txt','w')
# ln = open('/Users/anshu/Documents/sih/linkedin/linkedin_response.txt','w')
# gp = open('/home/ash/Desktop/Backend-SIH19FGAK2/saves/googleplus_response.txt','w')

if(data['meta']['http_code'] == 200):
    for post in data['posts']:
        #if(post['network'] == 'web' and post['url'] != '' and post['url'].find('facebook') != -1 and post['url'].find('public') == -1):
        #    fb.write(post['url']+'\n')
        if(post['url'] != '' and post['url'].find('facebook') != -1 and post['url'].find('public') == -1):
             fb.write(post['url']+'\n')
        #elif(post['network'] == 'web' and post['url'] != '' and post['url'].find('linkedin') != -1):
            #ln.write(post['url']+'\n')
        # elif(post['network'] == 'twitter' and post['user']['url'] != ''):
        #     tw.write(post['user']['url'] + '\n')
        # elif(post['network'] == 'googleplus' and post['user']['url'] != ''):
        #     gp.write(post['user']['url'] + '\n')
    print('Done writing URL(s)...')
    print('Starting scraping...')
elif(data['meta']['http_code'] == 400):
    print('Error 400 : Bad Request !')
elif(data['meta']['http_code'] == 401):
    print('Error 401 : Unauthorized !')
elif(data['meta']['http_code'] == 403):
    print('Error 403 : Requests limit exceeded !')
elif(data['meta']['http_code'] == 404):
    print('Error 404 : Data not found !')
elif(data['meta']['http_code'] == 405):
    print('Error 405 : Method not allowed !')
elif(data['meta']['http_code'] == 503):
    print('Error 503 : Service unavailable !')
else:
    print('HTTP response code :',data['meta']['http_code'])

print('Done scraping URL(s)...')

fb.close()
# tw.close()
# gp.close()
