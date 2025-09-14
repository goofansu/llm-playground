# https://github.com/senstella/parakeet-mlx
from parakeet_mlx import from_pretrained

model = from_pretrained("mlx-community/parakeet-tdt-0.6b-v3")
result = model.transcribe("2086-149220-0033.wav")
print(result.text)
