from mcp.server.fastmcp import FastMCP
from .jenkins_initializer import JenkinsInitializer

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def promote_mlx_crud_app(build: str, tenant_name: str) -> str:
    """
    Promote MLX-CRUD-APP build to required tenant
    :param build: The build version to promote - Do not assume, user must provide the build version
    :param tenant_name: The tenant to promote the build to accept "dev" or "int" -  mow-dev = dev; mow-int = int
    """
    jenkins = JenkinsInitializer()
    return jenkins.promote_mlx_crud_app(build, tenant_name)


@mcp.tool()
def promote_cml_config_store(build: str, tenant_name: str) -> str:
    """
    Promote CML-Config-Store build to required tenant
    :param build: The build version to promote - Do not assume, user must provide the build version
    :param tenant_name: The tenant to promote the build to accept "dev" or "int" -  mow-dev = dev; mow-int = int
    """
    jenkins = JenkinsInitializer()
    return jenkins.promote_cml_config_store(build, tenant_name)

@mcp.tool()
def integrate_mlxcrudapp_cdsw(branch: str = "master", cdsw_version: str = "latest") -> str:
    """
    Integrate MLX-CRUD-APP with CDSW
    :param branch: The MLX_CRUD_APP branch to integrate with CDSW, default is "master" - should be master or  in "1.x.0" or "mlx-crud-app-1.x.0" format" - User must provide this do not assume
    :param cdsw_version: The CDSW version to integrate with, default is "latest" - should be latest or in "2.0.x-bxxx" format - User must provide this do not assume
    """
    jenkins = JenkinsInitializer()
    return jenkins.integrate_mlxcrudapp_cdsw(branch, cdsw_version)

@mcp.tool()
def trigger_stage_promotion_tests() -> str:
    """Trigger stage promotion tests"""
    jenkins = JenkinsInitializer()
    return jenkins.trigger_stage_promotion_tests()

@mcp.tool()
def trigger_dev_promotion_tests() -> str:
    """Trigger dev promotion tests"""
    jenkins = JenkinsInitializer()
    return jenkins.trigger_dev_promotion_tests()

@mcp.tool()
def trigger_int_promotion_tests() -> str:
    """Trigger int promotion tests"""
    jenkins = JenkinsInitializer()
    return jenkins.trigger_int_promotion_tests()

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


def main():
    """Entry point for the MCP server"""
    # Use FastMCP's run method instead of creating a new Server
    mcp.run()


if __name__ == "__main__":
    main()
