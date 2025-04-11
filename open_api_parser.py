import json

def parse_openapi_spec(file_path):
    """
    Parse OpenAPI specification to detect endpoints.

    :param file_path: Path to the OpenAPI JSON file
    :return: List of endpoints with method, path, parameters, and category
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        openapi_spec = json.load(f)

    if 'paths' not in openapi_spec:
        raise Exception('Invalid OpenAPI specification: "paths" not found.')
    
    host = "http://examplex.com"
    if 'host' in openapi_spec:
        host = "http://"+openapi_spec['host'] 


    endpoints = []

    for path, methods in openapi_spec['paths'].items():
        for method, details in methods.items():
            parameters = detect_request_parameters(details)
            category = get_request_category(details)
            endpoints.append({
                'method': method.strip().lower(),
                'path': path.strip().lower(),
                'parameters': parameters,
                'category': category
            })

    return host, endpoints


def detect_request_parameters(details):
    """
    Detect request parameters for a given endpoint method.

    :param details: Method details (like parameters, description, etc.)
    :return: List of parameters (name, in, required, type, format)
    """
    parameters = []

    if 'parameters' in details and isinstance(details['parameters'], list):
        for param in details['parameters']:
            parameters.append({
                'name': param.get('name'),
                'in': param.get('in'),
                'required': param.get('required', False),
                'type': param.get('schema', {}).get('type', param.get('type', 'unknown type')),
                'format': param.get('schema', {}).get('format', param.get('format', 'unknown format'))
            })

    return parameters


def get_request_category(details):
    """
    Get the first tag (category) of the endpoint.

    :param details: Method details
    :return: First tag as string or empty string
    """
    return details.get('tags', [''])[0]


def print_endpoints(endpoints):
    """
    Pretty-print the endpoints list with formatted query strings.

    :param endpoints: List of endpoint dictionaries
    """
    for ep in endpoints:
        print(f"{ep['method']} {ep['path']}")
        print(f"Category: {ep['category']}")

        query_params = []

        if ep['parameters']:
            print("Parameters:")
            for param in ep['parameters']:
                print(f"- {param['name']} (in: {param['in']}, required: {param['required']}, type: {param['type']}, format: {param['format']})")
                
                if param['in'] == 'query':
                    # Add to query parameter list in key=value format
                    query_params.append(f"{param['name']}=value")

            # Print formatted query string if there are any query parameters
            if query_params:
                query_string = '&'.join(query_params)
                print(f"{ep['path']}?{query_string}")
        else:
            print("No parameters")
        
        print("-" * 40)


"""
if __name__ == "__main__":
    try:
        file_path = 'openapi.json'  # Adjust the path to your file
        endpoints = parse_openapi_spec(file_path)
        print_endpoints(endpoints)
    except Exception as e:
        print(f"Error: {e}")
"""