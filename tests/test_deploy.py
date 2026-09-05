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
            self.assertIn('Merchant of Oz', content)
            self.assertIn('signInWithPopup', content)
            self.assertIn('GoogleAuthProvider', content)
            self.assertIn('iron-hope-shop-ff854', content)
            self.assertIn('tamagui.css', content)
            self.assertIn('tamagui-theme.js', content)
            self.assertIn('t-nav', content)
            self.assertIn('t-drawer-nav', content)
            self.assertIn('view-home', content)
            self.assertIn('view-product', content)
            self.assertIn('view-cart', content)
            self.assertIn('view-settings', content)
            self.assertIn('settings-subpanel-themes', content)
            self.assertIn('settings-subpanel-account', content)
            self.assertIn('theme-controls-auth-panel', content)
            self.assertIn('theme-controls-guest-banner', content)
            self.assertIn('avatar-file-input', content)
            self.assertIn('build-watermark', content)
            self.assertIn('nav-guest-login-btn', content)
            self.assertIn('nav-profile-menu', content)
            self.assertIn('auth-prompt-modal', content)
            self.assertIn('handleRoute', content)
            # Unified Storefront & Pinterest collage elements on home
            self.assertIn('home-pinterest-grid', content)
            self.assertIn('pinterest-collage', content)
            self.assertIn('collage-pin', content)
            self.assertIn('collage-filter-bar', content)
            self.assertIn('hero-collage-banner', content)
            self.assertIn('products-catalog-container', content)
            self.assertIn('deal-ribbon', content)
            # Route guard check & auth prompt
            self.assertIn('openAuthModal', content)
            # Global AppAuth bridge
            self.assertIn('window.AppAuth', content)
            self.assertIn('AppAuth.signIn()', content)
            self.assertIn('AppAuth.signOut()', content)
            # Google Ads Styled spaces
            self.assertIn('ad-banner-slot', content)
            self.assertIn('ad-leaderboard', content)
            self.assertIn('ad-footer-unit', content)
            self.assertIn('ad-pin', content)
            self.assertIn('Sponsored Advertisement', content)
            # Immediate synchronous initialization & non-blank startup
            self.assertIn('renderHomePinterestCollage();', content)
            self.assertIn('renderCatalog();', content)
            # Ensure "Welcome back" was removed from Home
            self.assertNotIn('id="home-user-welcome"', content)

    def test_version_json_exists(self):
        self.assertTrue(os.path.exists('public/version.json'))
        with open('public/version.json', 'r') as f:
            content = f.read()
            self.assertIn('"buildNumber"', content)
            self.assertIn('"version"', content)

    def test_tamagui_css_design_system(self):
        self.assertTrue(os.path.exists('public/tamagui.css'))
        with open('public/tamagui.css', 'r') as f:
            content = f.read()
            # Verify design tokens
            self.assertIn('--space-4: 16px;', content)
            self.assertIn('--radius-4: 9px;', content)
            self.assertIn('--font-family-body:', content)
            
            # Verify themes & color scales
            self.assertIn('.t_light', content)
            self.assertIn('.t_dark', content)
            self.assertIn('[data-theme="dark"]', content)
            self.assertIn('--color-blue-9:', content)
            self.assertIn('--color-purple-9:', content)
            self.assertIn('--color-green-9:', content)
            self.assertIn('--color-red-9:', content)
            
            # Verify sub-themes
            self.assertIn('.t_blue', content)
            self.assertIn('.t_purple', content)
            self.assertIn('.t_green', content)
            self.assertIn('.t_red', content)
            self.assertIn('.t_orange', content)
            self.assertIn('.t_pink', content)
            self.assertIn('.t_yellow', content)

            # Verify Tamagui primitives
            self.assertIn('.t-ystack', content)
            self.assertIn('.t-xstack', content)
            self.assertIn('.t-zstack', content)
            self.assertIn('.t-group', content)
            self.assertIn('.t-card', content)
            self.assertIn('.t-btn', content)
            self.assertIn('.t-input', content)
            self.assertIn('.t-switch', content)
            self.assertIn('.t-badge', content)
            self.assertIn('.t-badge-warning', content)
            self.assertIn('.t-badge-yellow', content)
            self.assertIn('.t-badge-danger', content)
            self.assertIn('.t-badge-red', content)
            self.assertIn('.t-avatar', content)
            self.assertIn('.t-tooltip-primary', content)
            self.assertIn('.t-nav', content)
            self.assertIn('.t-drawer-layout', content)
            self.assertIn('.t-drawer-nav', content)

    def test_tamagui_theme_js_engine(self):
        self.assertTrue(os.path.exists('public/tamagui-theme.js'))
        with open('public/tamagui-theme.js', 'r') as f:
            content = f.read()
            self.assertIn('ThemeEngine', content)
            self.assertIn('setTheme', content)
            self.assertIn('setSubTheme', content)
            self.assertIn('toggleTheme', content)
            self.assertIn('subscribe', content)
            self.assertIn('data-theme', content)
            self.assertIn('data-subtheme', content)

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
