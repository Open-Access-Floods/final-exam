let map = L.map('map').setView([-30.0, -53.0], 6);

// Base map layer
L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://stamen.com">Stamen Design</a>',
  maxZoom: 20
}).addTo(map);

let currentLayer;
let tooltip = L.tooltip({ permanent: false, direction: "top", className: "custom-tooltip" });


function updateMap(dataset) {
  if (currentLayer) {
    map.removeLayer(currentLayer);
  }

  fetch('assets/VisualizationFiles/merged.geojson')
    .then(response => response.json())
    .then(data => {
      if (dataset === 'general') {
        currentLayer = L.geoJson(data, {
          style: styleGeneral,
          onEachFeature: onEachFeatureGeneral
        }).addTo(map);
      } else if (dataset === 'percentageAffected') {
        currentLayer = L.geoJson(data, {
          style: stylePercentage,
          onEachFeature: onEachFeaturePercentage
        }).addTo(map);
      }  else if (dataset === 'deaths') {
        currentLayer = L.geoJson(data, {
          style: styleDeaths,
          onEachFeature: onEachFeatureDeaths
        }).addTo(map);

      }  else if (dataset === 'injured') {
        currentLayer = L.geoJson(data, {
          style: styleInjured,
          onEachFeature: onEachFeatureInjured
        }).addTo(map);

      }  else if (dataset === 'sick') {
        currentLayer = L.geoJson(data, {
          style: styleSick,
          onEachFeature: onEachFeatureSick
        }).addTo(map);

      }  else if (dataset === 'missing') {
        currentLayer = L.geoJson(data, {
          style: styleMissing,
          onEachFeature: onEachFeatureMissing
        }).addTo(map);

      }  else if (dataset === 'evacuated') {
        currentLayer = L.geoJson(data, {
          style: styleEvacuated,
          onEachFeature: onEachFeatureEvacuated
        }).addTo(map);

      }  else if (dataset === 'displaced') {
        currentLayer = L.geoJson(data, {
          style: styleDisplaced,
          onEachFeature: onEachFeatureDisplaced
        }).addTo(map);

      }  else if (dataset === 'otherAffected') {
        currentLayer = L.geoJson(data, {
          style: styleOtherAffected,
          onEachFeature: onEachFeatureOtherAffected
        }).addTo(map);

      }
    })
    .catch(error => console.error('Error loading GeoJSON:', error));
}


function styleGeneral(feature) {
  return {
    fillColor: '#2594D9',
    weight: 1,
    color: 'white',
    fillOpacity: 0.9
  };
}


function onEachFeatureGeneral(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipGeneral(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}

function showTooltipGeneral(e, feature) {
  const props = feature.properties;
  const content = `
    <strong>${props.municipality}</strong><br/>
    Area: ${props.area} km²<br/>
    Pop. 2022: ${props.population2022}<br/>
    Pop. 2024: ${props.population2024}
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}

function stylePercentage(feature) {
  const pct = parseFloat(feature.properties.percentageAffected);
  return {
    fillColor: getColorByPercentage(pct),
    weight: 1,
    color: 'white',
    fillOpacity: 0.9
  };
}

function getColorByPercentage(pct) {
  if (pct === null || pct === undefined || isNaN(pct)) {
    return '#cccccc';
  }
  return pct > 80 ? '#164D00' :
         pct > 60 ? '#217620' :
         pct > 40 ? '#2EA746' :
         pct > 20 ? '#3DDE71' :
                    '#78FFA9';
}

function onEachFeaturePercentage(feature, layer) {
  layer.bindTooltip(function () {
    let div = L.DomUtil.create('div');

    let handleObject = val => {
      if (val === null || val === undefined) return '';
      if (typeof val === 'object') return JSON.stringify(val);
      return val;
    };

    let fields = ["municipality", "percentageAffected", "population2024", "totalAffected", "event"];
    let aliases = ["Municipality", "Affected Population (%)", "Estimated Pop. (2024)", "Total Affected Population", "Event"];

    let table = '<table>' +
      fields.map((field, i) =>
        `<tr>
          <th>${aliases[i]}</th>
          <td>${handleObject(feature.properties[field])}</td>
        </tr>`
      ).join('') +
      '</table>';

    div.innerHTML = table;
    return div;
  }, {
    sticky: true,
    className: "foliumtooltip",
    direction: 'top'
  });
}


function showTooltipPercentage(e, feature) {
  const props = feature.properties;
  const content = `
    <strong>Municipality:</strong> ${props.municipality}<br/>
    <strong>Estimated Pop. 2024:</strong> ${props.population2024}<br/>
    <strong>Affected Pop.:</strong> ${props.percentageAffected}%<br/>
    <strong>Event:</strong> ${props.event}
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}

function styleDeaths(feature) {
  const deaths = feature.properties.deaths;
  return {
    fillColor: getColorByDeaths(deaths),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByDeaths(d) {
  return d > 9 ? '#000000' :
         d > 6 ? '#333333' :
         d > 4 ? '#666666' :
         d > 1 ? '#999999' :
         d > 0 ? '#cccccc' :
                 '#ffffff'; // No data or 0 deaths
}


function onEachFeatureDeaths(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipDeaths(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipDeaths(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Deaths</th><td>${props.deaths}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}


function styleInjured(feature) {
  const injured = feature.properties.injured;
  return {
    fillColor: getColorByInjured(injured),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByInjured(d) {
  return d > 1000 ? '#D10E00' :
         d > 100 ? '#DC483D' :
         d > 50 ? '#E98B84' :
         d > 10 ? '#F2BCB8' :
         d > 1 ? '#FBEDEC' :
                 '#ffffff'; 
}


function onEachFeatureInjured(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipInjured(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipInjured(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Injured</th><td>${props.injured}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}


function styleSick(feature) {
  const sick = feature.properties.sick;
  return {
    fillColor: getColorBySick(sick),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorBySick(d) {
  return d > 1000 ? '#06127D' :
         d > 100 ? '#3A4498' :
         d > 50 ? '#838ABE' :
         d > 10 ? '#C8CCE2' :
         d > 1 ? '#E7E8F2' :
                 '#ffffff'; 
}


function onEachFeatureSick(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipSick(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipSick(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Sick</th><td>${props.sick}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}


function styleMissing(feature) {
  const missing = feature.properties.missing;
  return {
    fillColor: getColorByMissing(missing),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByMissing(d) {
  return d > 250 ? '#5C0156' :
         d > 100 ? '#7D3378' :
         d > 10 ? '#A26C9D' :
         d > 2 ? '#CAACC7' :
         d > 1 ? '#EADEE9' :
                 '#ffffff'; 
}


function onEachFeatureMissing(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipMissing(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipMissing(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Missing</th><td>${props.missing}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}


function styleEvacuated(feature) {
  const evacuated = feature.properties.evacuated;
  return {
    fillColor: getColorByEvacuated(evacuated),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByEvacuated(d) {
  return d > 100000 ? '#FFD900' :
         d > 20000 ? '#FFF200' :
         d > 5000 ? '#FFF97E' :
         d > 500 ? '#FFFBAD' :
         d > 1 ? '#FFFDD6' :
                 '#ffffff';
}


function onEachFeatureEvacuated(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipEvacuated(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipEvacuated(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Evacuated</th><td>${props.evacuated}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}


function styleDisplaced(feature) {
  const displaced = feature.properties.displaced;
  return {
    fillColor: getColorByDisplaced(displaced),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByDisplaced(d) {
  return d > 10000 ? '#FF9500' :
         d > 1000 ? '#FFBF66' :
         d > 500 ? '#FFD59B' :
         d > 100 ? '#FFEACC' :
         d > 1 ? '#FFF5E7' :
                 '#ffffff';
}


function onEachFeatureDisplaced(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipDisplaced(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipDisplaced(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>Displaced</th><td>${props.displaced}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}

function styleOtherAffected(feature) {
  const otherAffected = feature.properties.otherAffected;
  return {
    fillColor: getColorByOtherAffected(otherAffected),
    weight: 1,
    opacity: 1,
    color: '#cccccc',
    fillOpacity: 0.9
  };
}

function getColorByOtherAffected(d) {
  return d > 100000 ? '#8C0021' :
         d > 50000 ? '#B2556B' :
         d > 15000 ? '#C68091' :
         d > 500 ? '#DFB8C2' :
         d > 1 ? '#F1DFE4' :
                 '#ffffff';
}


function onEachFeatureOtherAffected(feature, layer) {
  layer.on({
    mouseover: function (e) {
      showTooltipOtherAffected(e, feature);
      e.target.setStyle({
        weight: 2,
        color: '#666',
        fillOpacity: 0.9
      });
    },
    mouseout: function (e) {
      map.closeTooltip(tooltip);
      currentLayer.resetStyle(e.target);
    },
    mousemove: function (e) {
      tooltip.setLatLng(e.latlng);
    }
  });
}


function showTooltipOtherAffected(e, feature) {
  const props = feature.properties;
  const content = `
    <div class="foliumtooltip">
      <table>
        <tr><th>Municipality</th><td>${props.municipality}</td></tr>
        <tr><th>Estimated Pop. 2024</th><td>${Number(props.population2024).toLocaleString()}</td></tr>
        <tr><th>OtherAffected</th><td>${props.otherAffected}</td></tr>
      </table>
    </div>
  `;
  tooltip.setContent(content);
  tooltip.setLatLng(e.latlng);
  tooltip.addTo(map);
}

// Load default layer
updateMap('general');
