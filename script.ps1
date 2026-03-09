# Projeto: Gerador de Homenagens com Streamlit

# Login na conta Azure
az login

# 2 - Variáveis utilizadas no projeto
$RESOURCE_GROUP="homenagem-rg"
$LOCATION="eastus"
$ENVIRONMENT="homenagem-env"
$ACR_NAME="acrhomenagemdio"
$APP_NAME="homenagem-streamlit-app"

# 3 - Criar Resource Group
az group create `
--name $RESOURCE_GROUP `
--location $LOCATION

# 4 - Criar Azure Container Registry
az acr create `
--name $ACR_NAME `
--resource-group $RESOURCE_GROUP `
--sku Basic `
--admin-enabled true

# 5 - Login no Azure Container Registry
az acr login --name $ACR_NAME

# 6 - Build da imagem Docker
docker build -t $ACR_NAME.azurecr.io/homenagem-app:latest .

# 7 - Enviar imagem para o Azure Container Registry
docker push $ACR_NAME.azurecr.io/homenagem-app:latest

# 8 - Criar ambiente do Azure Container Apps
az containerapp env create `
--name $ENVIRONMENT `
--resource-group $RESOURCE_GROUP `
--location $LOCATION

# 9 - Criar Container App
az containerapp create `
--name $APP_NAME `
--resource-group $RESOURCE_GROUP `
--environment $ENVIRONMENT `
--image $ACR_NAME.azurecr.io/homenagem-app:latest `
--target-port 8501 `
--ingress external `
--registry-server $ACR_NAME.azurecr.io `
--registry-username $ACR_NAME `
--registry-password (az acr credential show --name $ACR_NAME --query passwords[0].value -o tsv)

# 10 - Obter URL pública da aplicação
az containerapp show `
--name $APP_NAME `
--resource-group $RESOURCE_GROUP `
--query properties.configuration.ingress.fqdn

# 11 - Executar aplicação localmente com Docker
docker build -t homenagem-streamlit .

docker run -p 8501:8501 homenagem-streamlit