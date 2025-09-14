import mlx_whisper

result = mlx_whisper.transcribe(
    "2086-149220-0033.wav",
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
)

print(result["text"])
