/**
 * Tamagui Theme Engine Runtime (Zero Dependencies)
 * 
 * Provides theme management, sub-theme switching, system preference detection,
 * and event emission for theme changes.
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.TamaguiTheme = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  const THEME_STORAGE_KEY = 'tamagui_theme';
  const SUBTHEME_STORAGE_KEY = 'tamagui_subtheme';

  const validThemes = ['light', 'dark', 'system'];
  const validSubThemes = ['blue', 'purple', 'green', 'red', 'orange', 'pink', 'yellow'];

  class ThemeEngine {
    constructor() {
      this.listeners = new Set();
      this.theme = this.getStoredTheme() || 'system';
      this.subTheme = this.getStoredSubTheme() || 'blue';
      
      this.mediaQuery = (typeof window !== 'undefined' && window.matchMedia)
        ? window.matchMedia('(prefers-color-scheme: dark)')
        : null;

      if (this.mediaQuery) {
        this.mediaQuery.addEventListener('change', (e) => {
          if (this.theme === 'system') {
            this.applyTheme();
          }
        });
      }

      this.applyTheme();
    }

    getStoredTheme() {
      try {
        if (typeof localStorage !== 'undefined') {
          return localStorage.getItem(THEME_STORAGE_KEY);
        }
      } catch (e) {
        // Fallback if localStorage is inaccessible
      }
      return null;
    }

    getStoredSubTheme() {
      try {
        if (typeof localStorage !== 'undefined') {
          return localStorage.getItem(SUBTHEME_STORAGE_KEY);
        }
      } catch (e) {
        // Fallback
      }
      return null;
    }

    getResolvedTheme() {
      if (this.theme === 'system') {
        return (this.mediaQuery && this.mediaQuery.matches) ? 'dark' : 'light';
      }
      return this.theme;
    }

    setTheme(themeName) {
      if (!validThemes.includes(themeName)) {
        console.warn(`[TamaguiTheme] Invalid theme: ${themeName}. Supported: ${validThemes.join(', ')}`);
        return;
      }
      this.theme = themeName;
      try {
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem(THEME_STORAGE_KEY, themeName);
        }
      } catch (e) {}

      this.applyTheme();
      this.notify();
    }

    setSubTheme(subThemeName) {
      if (!validSubThemes.includes(subThemeName)) {
        console.warn(`[TamaguiTheme] Invalid sub-theme: ${subThemeName}. Supported: ${validSubThemes.join(', ')}`);
        return;
      }
      this.subTheme = subThemeName;
      try {
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem(SUBTHEME_STORAGE_KEY, subThemeName);
        }
      } catch (e) {}

      this.applyTheme();
      this.notify();
    }

    toggleTheme() {
      const currentResolved = this.getResolvedTheme();
      this.setTheme(currentResolved === 'dark' ? 'light' : 'dark');
    }

    applyTheme() {
      if (typeof document === 'undefined') return;

      const resolved = this.getResolvedTheme();
      const root = document.documentElement;

      // Set dataset attributes and classes for flexible CSS targeting
      root.setAttribute('data-theme', resolved);
      root.setAttribute('data-subtheme', this.subTheme);

      // Clean legacy/alternative classnames
      root.classList.remove('t_light', 't_dark');
      root.classList.add(`t_${resolved}`);

      validSubThemes.forEach(color => {
        root.classList.remove(`t_${color}`);
      });
      root.classList.add(`t_${this.subTheme}`);
    }

    subscribe(listener) {
      this.listeners.add(listener);
      return () => this.listeners.delete(listener);
    }

    notify() {
      const state = {
        theme: this.theme,
        resolvedTheme: this.getResolvedTheme(),
        subTheme: this.subTheme
      };
      this.listeners.forEach(fn => {
        try {
          fn(state);
        } catch (err) {
          console.error('[TamaguiTheme] Listener error:', err);
        }
      });
    }

    getState() {
      return {
        theme: this.theme,
        resolvedTheme: this.getResolvedTheme(),
        subTheme: this.subTheme,
        validThemes,
        validSubThemes
      };
    }
  }

  return new ThemeEngine();
}));
