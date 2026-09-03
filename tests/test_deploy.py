import unittest
import os
import re

class TestDeploymentSetup(unittest.TestCase):
    def test_dockerfile_exists(self):
        self.assertTrue(os.path.exists('Dockerfile'))
        with open('Dockerfile', 'r') as f:
            content = f.read()
            self.assertIn('FROM nginx:alpine', content)
            self.assertIn('EXPOSE 8080', content)

    def test_nginx_conf_proxy_and_healthz(self):
        self.assertTrue(os.path.exists('nginx.conf'))
        with open('nginx.conf', 'r') as f:
            content = f.read()
            self.assertIn('listen 8080;', content)
            self.assertIn('location /__/auth/', content)
            self.assertIn('proxy_pass https://iron-hope-shop-ff854.firebaseapp.com/__/auth/;', content)
            self.assertIn('location = /healthz', content)

    def test_public_html_exists(self):
        self.assertTrue(os.path.exists('public/index.html'))
        with open('public/index.html', 'r') as f:
            content = f.read()
            self.assertIn('Hello World', content)

    def test_firebase_config_exists(self):
        self.assertTrue(os.path.exists('firebase.json'))
        self.assertTrue(os.path.exists('.firebaserc'))
        with open('firebase.json', 'r') as f:
            content = f.read()
            self.assertIn('"public": "public"', content)
        with open('.firebaserc', 'r') as f:
            content = f.read()
            self.assertIn('"default": "iron-hope-shop-ff854"', content)

    def test_deploy_script_exists(self):
        self.assertTrue(os.path.exists('deploy-firebase.sh'))
        with open('deploy-firebase.sh', 'r') as f:
            content = f.read()
            self.assertIn('iron-hope-shop-ff854', content)
            self.assertIn('firebase-tools deploy', content)

    def test_github_workflow_exists(self):
        workflow_path = '.github/workflows/google-cloudrun-docker.yml'
        self.assertTrue(os.path.exists(workflow_path))
        with open(workflow_path, 'r') as f:
            content = f.read()
            self.assertIn('google-github-actions/auth@v2', content)
            self.assertIn('google-github-actions/deploy-cloudrun@v2', content)
            self.assertIn('SERVICE: merchant-of-oz', content)

if __name__ == '__main__':
    unittest.main()
