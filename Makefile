GRAFANA_TARGET_VERSION ?= main
SWAGGER_CODEGEN_CLI_TAG ?= latest
SWAGGER_SPEC_LOCAL ?= $$(pwd)/api-merged.json
PACKAGE_NAME = gpyclient

generate:
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v $$(pwd):$$(pwd) \
	swaggerapi/swagger-codegen-cli:${SWAGGER_CODEGEN_CLI_TAG} generate \
	-i https://raw.githubusercontent.com/grafana/grafana/${GRAFANA_TARGET_VERSION}/public/api-merged.json \
	-l python \
	-o $$(pwd)/${PACKAGE_NAME} \
	--model-name-suffix=Model \
	--additional-properties packageName=${PACKAGE_NAME} \
	-t $$(pwd)/codegen/templates

generate-local:
	docker run --rm \
	--user $$(id -u):$$(id -g) \
	-v $$(pwd):$$(pwd) \
	swaggerapi/swagger-codegen-cli:${SWAGGER_CODEGEN_CLI_TAG} generate \
	-i ${SWAGGER_SPEC_LOCAL} \
	-l python \
	-o $$(pwd)/${PACKAGE_NAME} \
	--model-name-suffix=Model \
	--additional-properties packageName=${PACKAGE_NAME} \
	-t $$(pwd)/codegen/templates

clean:
	rm -rf ${PACKAGE_NAME}