# Tracker
Tracker is a python package, that can be integrated into any django project as middleware. It asynchronously 
intercepts requests and sends metric data to our backend

### Editing settings
To make Tracker work properly, settings.py file should be modified

- Add the following line to the MIDDLEWARE (after all django middlewares:
```python
'rigidanalytics.middleware.Analytics',
```
- Add the following dict that configures Tracker
```python
RIGID_ANALYTICS = {
    'PROJECT_ID': '<id of your project>',
    'PROJECT_TOKEN': '<your project token>',
    'DEBUG_DISABLE_ANALYTICS': '<bool>',
    'BACKEND_ENDPOINT': '<custom endpoint, do not specify to use default>',
}
```