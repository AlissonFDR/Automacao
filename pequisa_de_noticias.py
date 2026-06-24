import time
from playwright.sync_api import sync_playwright


def testar_navegacao_google():
    print("Iniciando o teste no Nomus...")
    TERMO_PESQUISA = "Notícias do dia"  # ← Altere aqui
    try:
        with sync_playwright() as p:
 
            # ── PASSO 1: Abre o navegador ──────────────────────────
            # headless=False → abre janela visível (bom para testar)
            # headless=True  → roda invisível (ideal para serviço)
            print("Abrindo o navegador Chromium...")
            browser = p.chromium.launch(headless=False, channel="chrome")
            page = browser.new_page()
 
            # ── PASSO 2: Acessa o Google ───────────────────────────
            page.goto("https://www.google.com/?hl=pt-BR")
 
            # Aguarda a página carregar completamente antes de continuar
            page.wait_for_load_state("networkidle")
            print("Página do Google carregada com sucesso.")

            print(f"Digitando na barra de pesquisa: '{TERMO_PESQUISA}'...")
            search_box = page.get_by_role("combobox", name="Pesquisar")
            search_box.click()
            search_box.type(TERMO_PESQUISA)
            search_box.press("Enter")
            print("Pesquisa enviada. Aguardando resultados...")
 
            # ── PASSO 3: Clica no menu "Notícias" ─────────────────
            print("Procurando o link 'Notícias' no menu...")
 
            # Tenta clicar no link de Notícias com timeout de 5 segundos
            # Se não achar, cai no except e registra o erro
            page.get_by_role("link", name="Notícias").nth(0).click()
            print("Clique em 'Notícias' realizado.")
 
            # ── PASSO 4: Aguarda a página de notícias carregar ─────
            # Usando wait_for_load_state é mais confiável que time.sleep
            page.wait_for_load_state("networkidle")
            print("Página de Notícias carregada.")
            time.sleep(2)  # Pequena pausa visual para quem estiver assistindo
 
            # ── PASSO 5: Captura a primeira manchete ───────────────
            print("Buscando manchetes na página...")
 
            # Conta quantos elementos "heading" (títulos) existem na página
            total_elementos = page.get_by_role("heading").count()
            print(f"Total de headings encontrados: {total_elementos}")
 
            primeira_noticia = "Nenhuma notícia encontrada"
 
            if total_elementos >= 2:
                # O índice 0 costuma ser o título da página (ex: "Notícias")
                # O índice 1 em diante são as manchetes reais
                primeira_noticia = page.get_by_role("heading").nth(1).text_content()
 
            # ── PASSO 6: Exibe e salva o resultado ─────────────────
            print("-" * 50)
            print("AUTOMAÇÃO CONCLUÍDA COM SUCESSO!")
            print(f"Primeira manchete encontrada: {primeira_noticia}")
            print("-" * 50)
 
            # Mantém aberto 3 segundos para você ver o resultado na tela
            time.sleep(3)
            browser.close()
            print("Navegador fechado.")
 
    except Exception as e:
        # Se qualquer coisa der errado, registra o erro no print
        # Isso é essencial quando rodar como serviço (sem ninguém olhando)
        print(f"ERRO durante a automação: {str(e)}")
 
 


if __name__ == "__main__":
    testar_navegacao_google()