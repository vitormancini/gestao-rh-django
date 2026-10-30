class AjaxHandler {
    constructor(baseUrl = '') {
        this.baseUrl = baseUrl;

        this.defaultHeaders = {
            'Content-Type': 'application/json',
        }
    }

    // Define headers personalizados
    setHeader(key, value) {
        this.defaultHeaders[key] = value;
        return this;
    }

    // Monta a URL completa
    _buildURL(endpoint) {
        return `${this.baseUrl}${endpoint}`;
    }

    async _request(method, endpoint, data = null) {
        const config = {
            method,
            headers: { ...this.defaultHeaders },
        };

        if (data && ['POST', 'PUT', 'PATCH'].includes(method)) {
            config.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(this._buildURL(endpoint), config);

            // Tenta parsear JSON; se falhar, retorna texto
            let responseData;
            const contentType = response.headers.get('Content-Type') || '';

            if (contentType.includes('application/json')) {
                responseData = await response.json();
            } else {
                responseData = await response.text();
            }

            if (!response.ok) {
                throw {
                    status: response.status,
                    statusText: response.statusText,
                    data: responseData,
                };
            }

            return {
                status: response.status,
                data: responseData,
            };
        } catch (error) {
            console.error(`[AjaxHandler] ${method} ${endpoint} →`, error);
            throw error;
        }
    }

    async get(endpoint) {
        return this._request('GET', endpoint);
    }

    async post(endpoint, data) {
        return this._request('POST', endpoint, data);
    }

    async put(endpoint, data) {
        return this._request('PUT', endpoint, data);
    }

    async delete(endpoint) {
        return this._request('DELETE', endpoint);
    }
}