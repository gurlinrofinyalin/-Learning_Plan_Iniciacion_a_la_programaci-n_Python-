# Jerarquia de servidores DNS
servidores = {
    "root": {
        "com": "servidor_tld",  # Redirige a .com
        "org": "servidor_org_tld"  # ejemplo que no vale
    },
    "servidor_tld": {
        "google.com": "ns1.google.com",  # Redirige al autoritativo
        "example.com": "ns1.example.com"  # ejemplo que no vale
    },
    "ns1.google.com": {
        "google.com": "142.250.190.78"  # Respuesta autoritativa
    }
}


def dns_recursivo(dominio, servidor_actual="root"):
    print(f"[Recursivo] Consultando a {servidor_actual} para {dominio}")

    if servidor_actual not in servidores:
        return "Servidor no encontrado"

    #  El servidor actual tiene la respuesta directa (IP)
    if dominio in servidores[servidor_actual]:
        respuesta = servidores[servidor_actual][dominio]
        # Si es una IP (no empieza con "ns"), la devolvemos
        if not respuesta.startswith("ns"):
            return respuesta
        # Si es un servidor (empieza con "ns"), seguimos consultando
        else:
            return dns_recursivo(dominio, respuesta)

    #  Buscar por TLD (para servidores root y TLD)
    partes_dominio = dominio.split(".")
    tld = partes_dominio[-1]

    print(servidor_actual)
    if tld in servidores[servidor_actual]:
        siguiente_servidor = servidores[servidor_actual][tld]
        return dns_recursivo(dominio, siguiente_servidor)

    #  Dominio no encontrado
    return "Dominio no encontrado"



print("Resultado recursivo:", dns_recursivo("google.com"))
"""
tld es com
primero cliente consulta al servidor raiz, root
el servidor raiz ,root  consulta al servidor servidor_tld com
servidor_tld com  consulta al servidor autoritativo   ns1.example.com

LA SALIDA
[Recursivo] Consultando a root para google.com
[Recursivo] Consultando a servidor_tld para google.com
[Recursivo] Consultando a ns1.google.com para google.com
 Resultado recursivo: 142.250.190.78
"""

print('-----------------------')
print('-----------------------')
print('-----------------------')

# Simulación de servidores DNS (misma estructura que antes)
servidores = {
    "root": {
        "com": "servidor_tld",
        "org": "servidor_org_tld"
    },
    "servidor_tld": {
        "google.com": "ns1.google.com",
        "example.com": "ns1.example.com" # ejemplo que no vale
    },
    "ns1.google.com": {
        "google.com": "142.250.190.78"  # Registro A (IPv4)
    }
}


def dns_iterativo(dominio):
    servidor_actual = "root"
    intentos_maximos = 3  # Para evitar bucles infinitos
    intentos = 0

    print(f"\n[Iterativo] Búsqueda iniciada para: {dominio}")

    while intentos < intentos_maximos:   # 3 intentos
        intentos += 1
        print(f"  Intento {intentos}: Consultando a {servidor_actual}")

        #  Verificar si el servidor existe en la lista de servidores
        if servidor_actual not in servidores:
            print("  Servidor no encontrado en la jerarquía DNS")
            return None

        # Buscar el dominio (google terra ) o su TLD  (com org)
        if dominio in servidores[servidor_actual]:
            respuesta = servidores[servidor_actual][dominio]

            #  - Si es una IP (respuesta final)
            if not respuesta.startswith("ns") and respuesta.count(".") == 3:
                print(f"  ¡Respuesta autoritativa encontrada en {servidor_actual}!")
                return respuesta

            # - Si es otro servidor (delegación)
            servidor_actual = respuesta

        else:
            # - Buscar por TLD como fallback (para root y TLDs)
            tld = dominio.split(".")[-1]
            if tld in servidores[servidor_actual]:
                servidor_actual = servidores[servidor_actual][tld]
            else:
                print("  Dominio no encontrado en este servidor")
                return None

    print("  Límite de saltos alcanzado (posible bucle)")
    return None


print("Resultado para google.com:", dns_iterativo("google.com"))
print("\nResultado para example.com:", dns_iterativo("example.com"))
print("\nResultado para dominio_inexistente.com:", dns_iterativo("dominio_inexistente.com"))

"""
 
[Iterativo] Búsqueda iniciada para: google.com
  Intento 1: Consultando a root
  Intento 2: Consultando a servidor_tld
  Intento 3: Consultando a ns1.google.com
  ¡Respuesta autoritativa encontrada en ns1.google.com!
Resultado para google.com: 142.250.190.78


[Iterativo] Búsqueda iniciada para: example.com
  Intento 1: Consultando a root
  Intento 2: Consultando a servidor_tld
  Intento 3: Consultando a ns1.example.com
  Servidor no encontrado en la jerarquía DNS
Resultado para example.com: None


[Iterativo] Búsqueda iniciada para: dominio_inexistente.com
  Intento 1: Consultando a root
  Intento 2: Consultando a servidor_tld
  Dominio no encontrado en este servidor
Resultado para dominio_inexistente.com: None
"""
