import os
import sys
from PIL import Image

def optimize_image(input_path, output_path, max_width=1920, quality=80):
    """
    Otimiza uma imagem para uso web:
    - Redimensiona se for muito grande
    - Converte para WebP (formato eficiente)
    - Aplica compressão
    """
    try:
        if not os.path.exists(input_path):
            print(f"❌ Erro: Arquivo não encontrado: {input_path}")
            return False

        print(f"🔄 Processando: {input_path}")
        
        # Abrir imagem
        with Image.open(input_path) as img:
            # Converter para RGB se necessário (ex: PNG com transparência para JPG, mas WebP suporta alpha)
            # Para WebP, não precisamos descartar alpha, mas vamos garantir modo compatível
            
            # Calcular novas dimensões mantendo aspect ratio
            width, height = img.size
            if width > max_width:
                ratio = max_width / width
                new_height = int(height * ratio)
                print(f"📉 Redimensionando de {width}x{height} para {max_width}x{new_height}...")
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Salvar como WebP
            print(f"💾 Salvando em: {output_path}")
            img.save(output_path, 'WEBP', quality=quality, method=6)
            
            # Comparar tamanhos
            original_size = os.path.getsize(input_path) / (1024 * 1024)
            new_size = os.path.getsize(output_path) / (1024 * 1024)
            reduction = (1 - new_size / original_size) * 100
            
            print(f"✅ Sucesso! Otimização concluída.")
            print(f"   Tamanho Original: {original_size:.2f} MB")
            print(f"   Novo Tamanho:     {new_size:.2f} MB")
            print(f"   Redução:          {reduction:.1f}%")
            return True

    except Exception as e:
        print(f"❌ Erro fatal: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python optimize_image.py <caminho_da_imagem_gigante>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    filename = os.path.basename(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    
    # Caminho de saída padrão: pasta web/public/assets
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "web/public/assets")
    output_file = os.path.join(output_dir, f"{name_without_ext}_optimized.webp")
    
    optimize_image(input_file, output_file)
