# MACHINE-LEARNING-PROJECT

1. [Git_hub_Account] (https://github.com/)
2. [Heroku_Account] (https://www.heroku.com/)
3. [VS_CODE_IDE] (https://code.visualstudio.com/download)
4. [Git_clone] (https://github.com/maheshkammineni/MACHINE-LEARNING-PROJECT.git)

'''Creating conda environment:
conda create -p venv python==3.7 -y'''
'''

''' activate conda environment

conda activate venv/ 
conda.bat activate
'''



pip install -r requirements.txt '''

''''To add files to git

git add .

To ignore file or folder from git we can write a name or a folder in gitignore file

To check the git status
git status
To check allversion maintained by git
git log
To create version/commite all changes by git
git commit -m "message" '''

To setup CI/CD pipeline we need three information:
1. Heroku_email=  dspractice.mk@yahoo.com
2. Heroku_APIkey=  from api key app
3. Heroku_Appname= ml-regression-app1


Build docker image
'''
docker buid -t <image_name>:<tag_name>
'''
note: docker name image shpuld be in lowercase

To list docker images:
docker images

To run the docker image
docker run -p 5000:5000 -e PORT=5000 2a0673058b3f

To check running container in docker
'''
docker ps
'''
TO stop docker image: 

docker stop comtainer_id






