using System;
using TMPro;
using UnityEngine;

public class UI : MonoBehaviour
{
    [SerializeField]
    TextMeshProUGUI chatResponseText;

    [SerializeField]
    TMP_InputField contentInput;

    public async void CreateManagerButton()
    {
        var request = new JsonStructures.ChatInitRequest
        {
            context = contentInput.text
        };


        try
        {
            // Espera la respuesta (ya en el hilo principal)
            string json = await HttpWrap.SendPostRequest("/chat/init", request);

            JsonStructures.ChatInitResponse response =
                JsonUtility.FromJson<JsonStructures.ChatInitResponse>(json);

            // ? UI actualizada en el hilo principal
            chatResponseText.text = "Chat ID: " + response.chatId;
        }
        catch (Exception ex)
        {
            Debug.LogError("Error: " + ex.Message);
        }
    }
    
}
