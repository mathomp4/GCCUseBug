module base

{% for n in range(1, num_modules+1) -%}
use module{{n}}
{% endfor %}

end module base