using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

public static class HttpWrap
{
    const string base_url = "http://10.0.4.60:8000";

    private static readonly HttpClient client = new HttpClient();

    public static async Task<string> SendGetRequest(string url)
    {
        string ret;
        ret = await client.GetStringAsync(base_url + url);

        return ret;
    }
}
