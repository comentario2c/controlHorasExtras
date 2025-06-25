document.addEventListener('DOMContentLoaded', () => {
  // Mapeo de inputs a IDs de previsualización
  const campos = {
    'id_Nombre': 'preview-name',
    'id_fecha_contrato': 'preview-date',
    'id_monto_base': 'preview-base',
    'id_bono_produccion': 'preview-bonus',
    'id_tipo': 'preview-Tipo',
  };

  // Actualizar previews
  Object.keys(campos).forEach(id => {
    const input = document.getElementById(id);
    const preview = document.getElementById(campos[id]);

    if (input && preview) {
      const actualizar = () => {
        let valor = input.value;

        // Formato de dinero
        if (id.includes('monto_base') || id.includes('bono_produccion')) {
          valor = '$' + (parseFloat(valor) || 0).toLocaleString();
        }
        
        // Formato de fecha
        if (id.includes('fecha_contrato') && valor) {
            const [año, mes, día] = valor.split('-');
            valor = `${día}/${mes}/${año}`;
        }

        preview.textContent = valor || '-';
      };

      input.addEventListener('input', actualizar);
      actualizar();  // Inicial 
    }
  });

  // Calcular salario estimado con bono
  const baseInput = document.getElementById('id_monto_base');
  const bonoInput = document.getElementById('id_bono_produccion');
  const salarioPreview = document.getElementById('preview-salary');
  const horaOrdinaria = document.getElementById('preview-regular');
  const horaExtra = document.getElementById('preview-hora-extra-volver-preview');

function actualizarSalario() {
  const base = parseFloat(baseInput.value) || 0;
  const bono = parseFloat(bonoInput.value) || 0;
  const salario = base + bono;

  salarioPreview.textContent = '$' + salario.toLocaleString();

  const valorHora = (((salario) / 30) * 28) / 180;
  horaOrdinaria.textContent = '$' + valorHora.toFixed(2);
  horaExtra.textContent = '$' + (valorHora * 2).toFixed(2);
}

  if (baseInput && bonoInput && horaExtra) {
    baseInput.addEventListener('input', actualizarSalario);
    bonoInput.addEventListener('input', actualizarSalario);
    actualizarSalario();
  }
});