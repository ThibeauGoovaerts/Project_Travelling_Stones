import axios from "axios";
import type { AxiosInstance } from "axios";
import URL from "@/ApiAxios";

const apiClient: AxiosInstance = axios.create({
    baseURL: URL + ":8888/api",
    headers: {
        "Content-type": "application/json",
    },
});

export default apiClient;
