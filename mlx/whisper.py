import mlx_whisper

result = mlx_whisper.transcribe(
    "/Users/james/tmp/output.wav",
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
)

print(result)
