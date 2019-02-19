# Configuration file for jupyter-kernel-gateway.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = ''

## Specify a config file to load.
#c.JupyterApp.config_file_name = ''

## Generate default config file.
#c.JupyterApp.generate_config = False

#------------------------------------------------------------------------------
# KernelGatewayApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Application that provisions Jupyter kernels and proxies HTTP/Websocket traffic
#  to the kernels.
#  
#  - reads command line and environment variable settings - initializes managers
#  and routes - creates a Tornado HTTP server - starts the Tornado event loop

## Sets the Access-Control-Allow-Credentials header. (KG_ALLOW_CREDENTIALS env
#  var)
#c.KernelGatewayApp.allow_credentials = ''

## Sets the Access-Control-Allow-Headers header. (KG_ALLOW_HEADERS env var)
#c.KernelGatewayApp.allow_headers = ''

## Sets the Access-Control-Allow-Methods header. (KG_ALLOW_METHODS env var)
#c.KernelGatewayApp.allow_methods = ''

## Sets the Access-Control-Allow-Origin header. (KG_ALLOW_ORIGIN env var)
#c.KernelGatewayApp.allow_origin = ''

## Controls which API to expose, that of a Jupyter notebook server, the seed
#  notebook's, or one provided by another module, respectively using values
#  'kernel_gateway.jupyter_websocket', 'kernel_gateway.notebook_http', or another
#  fully qualified module name (KG_API env var)
#c.KernelGatewayApp.api = 'kernel_gateway.jupyter_websocket'

## Authorization token required for all requests (KG_AUTH_TOKEN env var)
#c.KernelGatewayApp.auth_token = ''

## The base path for mounting all API resources (KG_BASE_URL env var)
#c.KernelGatewayApp.base_url = '/'

## The full path to an SSL/TLS certificate file. (KG_CERTFILE env var)
#c.KernelGatewayApp.certfile = None

## The full path to a certificate authority certificate for SSL/TLS client
#  authentication. (KG_CLIENT_CA env var)
#c.KernelGatewayApp.client_ca = None

## Default kernel name when spawning a kernel (KG_DEFAULT_KERNEL_NAME env var)
#c.KernelGatewayApp.default_kernel_name = ''

## Environment variables allowed to be inherited from the spawning process by the
#  kernel
#c.KernelGatewayApp.env_process_whitelist = []

## Sets the Access-Control-Expose-Headers header. (KG_EXPOSE_HEADERS env var)
#c.KernelGatewayApp.expose_headers = ''

## Override any kernel name specified in a notebook or request
#  (KG_FORCE_KERNEL_NAME env var)
#c.KernelGatewayApp.force_kernel_name = ''

## IP address on which to listen (KG_IP env var)
#c.KernelGatewayApp.ip = '127.0.0.1'

## The kernel manager class to use.
#c.KernelGatewayApp.kernel_manager_class = 'kernel_gateway.services.kernels.manager.SeedingMappingKernelManager'

## The kernel spec manager class to use. Should be a subclass of
#  `jupyter_client.kernelspec.KernelSpecManager`.
#c.KernelGatewayApp.kernel_spec_manager_class = 'jupyter_client.kernelspec.KernelSpecManager'

## The full path to a private key file for usage with SSL/TLS. (KG_KEYFILE env
#  var)
#c.KernelGatewayApp.keyfile = None

## Sets the Access-Control-Max-Age header. (KG_MAX_AGE env var)
#c.KernelGatewayApp.max_age = ''

## Limits the number of kernel instances allowed to run by this gateway.
#  Unbounded by default. (KG_MAX_KERNELS env var)
#c.KernelGatewayApp.max_kernels = None

## Port on which to listen (KG_PORT env var)
#c.KernelGatewayApp.port = 8888

## Number of ports to try if the specified port is not available (KG_PORT_RETRIES
#  env var)
#c.KernelGatewayApp.port_retries = 50

## Number of kernels to prespawn using the default language. No prespawn by
#  default. (KG_PRESPAWN_COUNT env var)
#c.KernelGatewayApp.prespawn_count = None

## Runs the notebook (.ipynb) at the given URI on every kernel launched. No seed
#  by default. (KG_SEED_URI env var)
#c.KernelGatewayApp.seed_uri = None

## Use x-* header values for overriding the remote-ip, useful when application is
#  behing a proxy. (KG_TRUST_XHEADERS env var)
#c.KernelGatewayApp.trust_xheaders = False

#------------------------------------------------------------------------------
# NotebookHTTPPersonality(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Personality for notebook-http support, creating REST endpoints based on the
#  notebook's annotated cells

## Optional API to download the notebook source code in notebook-http mode,
#  defaults to not allow
#c.NotebookHTTPPersonality.allow_notebook_download = False

## Determines which module is used to parse the notebook for endpoints and
#  documentation. Valid module names include
#  'kernel_gateway.notebook_http.cell.parser' and
#  'kernel_gateway.notebook_http.swagger.parser'. (KG_CELL_PARSER env var)
#c.NotebookHTTPPersonality.cell_parser = 'kernel_gateway.notebook_http.cell.parser'

## Maps kernel language to code comment syntax
#c.NotebookHTTPPersonality.comment_prefix = {'scala': '//', None: '#'}

## Serve static files on disk in the given path as /public, defaults to not serve
#c.NotebookHTTPPersonality.static_path = None

#------------------------------------------------------------------------------
# JupyterWebsocketPersonality(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Personality for standard websocket functionality, registering endpoints that
#  are part of the Jupyter Kernel Gateway API

## Environment variables allowed to be set when a client requests a new kernel
#c.JupyterWebsocketPersonality.env_whitelist = []

## Permits listing of the running kernels using API endpoints /api/kernels and
#  /api/sessions (KG_LIST_KERNELS env var). Note: Jupyter Notebook allows this by
#  default but kernel gateway does not.
#c.JupyterWebsocketPersonality.list_kernels = False
