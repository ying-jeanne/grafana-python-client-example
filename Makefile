GRAFANA_TARGET_VERSION ?= main
SWAGGER_CODEGEN_CLI_TAG ?= latest
SWAGGER_SPEC_LOCAL ?= $$(pwd)/../grafana/public/api-merged.json

generate:
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v $$(pwd):$$(pwd) \
	swaggerapi/swagger-codegen-cli:${SWAGGER_CODEGEN_CLI_TAG} generate \
	-i https://raw.githubusercontent.com/grafana/grafana/${GRAFANA_TARGET_VERSION}/public/api-merged.json \
	-l python \
	-o $$(pwd)/pythonclient \
	--model-name-suffix=Model \
	--additional-properties packageName=pythonclient \
	-t $$(pwd)/codegen/templates