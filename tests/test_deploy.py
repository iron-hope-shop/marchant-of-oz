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

    def test_github_workflow_exists(self):
        self.assertTrue(os.path.exists('.github/workflows/deploy.yml'))
        with open('.github/workflows/deploy.yml', 'r') as f:
            content = f.read()
            self.assertIn('google-github-actions/auth@v2', content)
            self.assertIn('google-github-actions/deploy-cloudrun@v2', content)

if __name__ == '__main__':
    unittest.main()
