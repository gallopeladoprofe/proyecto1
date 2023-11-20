from conexion.Conexion import Conexion

class CiudadDao:
    
    def getCiudades(self):
        
        ciudadSQL = """
            SELECT id, descripcion
            FROM ciudades
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
            
    def insertCiudad(self, descripcion):
        
        insertSQL = """
            INSERT INTO ciudades(descripcion) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(insertSQL, (descripcion,))
            con.commit()
            return True
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()
        return False