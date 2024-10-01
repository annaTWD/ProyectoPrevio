# main.py
from models.rag import ChatPDF

def main():
    # Crear una instancia de la clase ChatPDF
    chat_pdf = ChatPDF(llm_model="qwen2.5")  # Puedes cambiar el modelo si lo deseas

    # Pide al usuario que ingrese la ruta del archivo PDF
    pdf_path = input("Por favor, ingrese la ruta del archivo PDF: ")

    # Ingresa el PDF en el sistema para ser procesado
    print(f"Ingestando el archivo PDF: {pdf_path}")
    chat_pdf.ingest(pdf_path)
    print("Archivo PDF procesado exitosamente.")

    # Bucle para hacer preguntas hasta que el usuario quiera salir
    while True:
        # Obtener la pregunta del usuario
        query = input("\nHaz una pregunta sobre el documento (o escribe 'salir' para finalizar): ")

        # Salir si el usuario escribe 'salir'
        if query.lower() == "salir":
            print("Saliendo del programa.")
            break

        # Hacer la pregunta al modelo y obtener la respuesta
        print("Procesando la pregunta...")
        response = chat_pdf.ask(query)
        print(f"Respuesta: {response}")

if __name__ == "__main__":
    main()
