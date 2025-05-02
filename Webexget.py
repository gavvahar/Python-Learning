import requests

class WebexAPIClient:
    def __init__(self, access_token):
        self.base_url = "https://webexapis.com/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    def get(self, path, params=None):
        url = f"{self.base_url}/{path}"
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


if __name__ == "__main__":
    # Replace with your actual token
    ACCESS_TOKEN = "MjE3MGQ2MjUtZGFjNy00MDA3LTkwMjQtYWMxZWIxM2Y1MmQxOGVlODYwZmYtZjA4_P0A1_046a3b8a-8fa8-4d4b-8523-dd06a1c17f85"
    client = WebexAPIClient(ACCESS_TOKEN)

    # 1. List all data sources
    print("\n🔹 All Data Sources:")
    data_sources = client.get("dataSources")
    print(data_sources)

    # 2. Get a specific data source by ID
    data_source_id = "dataSourceId"
    print(f"\n🔹 Data Source Details for ID: {data_source_id}")
    one_data_source = client.get(f"dataSources/{data_source_id}")
    print(one_data_source)

    # 3. List all schemas
    print("\n🔹 All Schemas:")
    schemas = client.get("dataSources/schemas")
    print(schemas)

    # 4. Get a specific schema by ID
    schema_id = "schemaId"
    print(f"\n🔹 Schema Details for ID: {schema_id}")
    one_schema = client.get(f"dataSources/schemas/{schema_id}")
    print(one_schema)