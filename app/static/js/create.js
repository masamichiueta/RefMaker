// 
//	jQuery Validate example script
//
//	Prepared by David Cochran
//	
//	Free for your use -- No warranties, no guarantees!
//

$(document).ready(function(){

	
		$('#form-article').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      journal: {
	        required: true,
	        minlength: 1
	        
	      },
	      title: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      note: {
	        required: false,
	        minlength: 0
	        
	      },
	      number: {
	      	minlength: 0,
	        required: false
	      },
	      pages: {
	        minlength: 0,
	        required: false
	      },
	      volume: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-book').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      title: {
	        required: true,
	        minlength: 1
	        
	      },
	      publisher: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
		    minlength: 1,
		    required: true
	      },
	      volume: {
	        minlength: 0,
	        required: false
	      },
	      number: {
		    minlength: 0,
		    required: false
	      },
	      address: {
	        required: false,
	        minlength: 0,
	        
	      },
	      edition: {
	      	minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-booklet').validate({
	    rules: {
	      title: {
	        minlength: 1,
	        required: true
	      },
	      address: {
	        required: false,
	        minlength: 0
	        
	      },
	      author: {
	      	minlength: 0,
	        required: false
	      },
	      howpublished: {
	        minlength: 0,
	        required: false
	      },
	      month: {
	        required: false,
	        minlength: 0,
	        
	      },
	      note: {
	      	minlength: 0,
	        required: false
	      },
	      year: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-inbook').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      chapter: {
	        required: true,
	        minlength: 1
	        
	      },
	      publisher: {
	      	minlength: 1,
	        required: true
	      },
	      title: {
	        minlength: 1,
	        required: true
	      },
	      year: {
	        required: true,
	        minlength: 1
	        
	      },
	      volume: {
	      	minlength: 0,
	        required: false
	      },
	      number: {
	      	minlength: 0,
	        required: false
	      },

	      address: {
	        minlength: 0,
	        required: false
	      },
	      edition: {
	        minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	        minlength: 0,
	        required: false
	      },
	      type: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-incollection').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      booktitle: {
	        required: true,
	        minlength: 1
	        
	      },
	      publisher: {
	      	minlength: 1,
	        required: true
	      },
	      title: {
	        minlength: 1,
	        required: true
	      },
	      year: {
	        required: true,
	        minlength: 1
	        
	      },
	      volume: {
	      	minlength: 0,
	        required: false
	      },
	      number: {
	      	minlength: 0,
	        required: false
	      },
	      address: {
	        minlength: 0,
	        required: false
	      },
	      chapter: {
	        minlength: 0,
	        required: false
	      },
	      edition: {
	        minlength: 0,
	        required: false
	      },
	      editor: {
	      	minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      pages: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	      	minlength: 0,
	        required: false
	      },
	      type: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  
	  $('#form-inproceedings').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      booktitle: {
	        required: true,
	        minlength: 1
	        
	      },
	      title: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      volume: {
	        required: false,
	        minlength: 0
	        
	      },
	      number: {
	        required: false,
	        minlength: 0
	      },
	      address: {
	      	minlength: 0,
	        required: false
	      },
	      editor: {
	        minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      organization: {
	      	minlength: 0,
	        required: false
	      },
	      pages: {
	        minlength: 0,
	        required: false
	      },
	      publisher: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-conference').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      booktitle: {
	        required: true,
	        minlength: 1
	        
	      },
	      title: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      volume: {
	        required: false,
	        minlength: 0
	        
	      },
	      number: {
	        required: false,
	        minlength: 0
	      },
	      address: {
	      	minlength: 0,
	        required: false
	      },
	      editor: {
	        minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      organization: {
	      	minlength: 0,
	        required: false
	      },
	      pages: {
	        minlength: 0,
	        required: false
	      },
	      publisher: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-manual').validate({
	    rules: {
	      title: {
	        minlength: 1,
	        required: true
	      },
	      address: {
	        required: false,
	        minlength: 1
	        
	      },
	      author: {
	      	minlength: 0,
	        required: false
	      },
	      edition: {
	        minlength: 0,
	        required: false
	      },
	      month: {
	        required: false,
	        minlength: 0
	        
	      },
	      note: {
	      	minlength: 0,
	        required: false
	      },
	      organization: {
	        minlength: 0,
	        required: false
	      },
	      year: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-masterthesis').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      school: {
	        required: true,
	        minlength: 1
	        
	      },
	      title: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      address: {
	        required: false,
	        minlength: 0
	        
	      },
	      month: {
	      	minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      type: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-misc').validate({
	    rules: {
	      author: {
	        minlength: 0,
	        required: false
	      },
	      title: {
	        required: false,
	        minlength: 0
	        
	      },
	      howpublished: {
	      	minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      year: {
	        required: false,
	        minlength: 0
	        
	      },
	      note: {
	      	minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-phdthesis').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      school: {
	        required: true,
	        minlength: 1
	        
	      },
	      title: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      address: {
	        required: false,
	        minlength: 0
	        
	      },
	      month: {
	      	minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      type: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-proceedings').validate({
	    rules: {
	      title: {
	        minlength: 1,
	        required: true
	      },
	      year: {
	        required: true,
	        minlength: 1
	        
	      },
	      volume: {
	      	minlength: 0,
	        required: false
	      },
	      number: {
	      	minlength: 0,
	        required: false
	      },
	      address: {
	        minlength: 0,
	        required: false
	      },
	      editor: {
	        required: false,
	        minlength: 0,
	        
	      },
	      note: {
	      	minlength: 0,
	        required: false
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      organization: {
	        minlength: 0,
	        required: false
	      },
	      publisher: {
	        minlength: 0,
	        required: false
	      },
	      series: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-techreport').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      title: {
	        required: true,
	        minlength: 1
	        
	      },
	      institution: {
	      	minlength: 1,
	        required: true
	      },
	      year: {
	        minlength: 1,
	        required: true
	      },
	      address: {
	        required: false,
	        minlength: 0
	        
	      },
	      month: {
	      	minlength: 0,
	        required: false
	      },
	      note: {
	        minlength: 0,
	        required: false
	      },
	      number: {
	        minlength: 0,
	        required: false
	      },
	      type: {
	        minlength: 0,
	        required: false
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
	  
	  $('#form-unpublished').validate({
	    rules: {
	      author: {
	        minlength: 1,
	        required: true
	      },
	      title: {
	        required: true,
	        minlength: 1
	        
	      },
	      note: {
	      	minlength: 1,
	        required: true
	      },
	      month: {
	        minlength: 0,
	        required: false
	      },
	      year: {
	        required: false,
	        minlength: 0
	      },
	    },
	    highlight: function(label) {
	    	$(label).closest('.control-group').addClass('error');
	    },
	    success: function(label) {
	    	label
	    		.text('OK!').addClass('valid')
	    		.closest('.control-group').addClass('success');
	    }
	  });
}); // end document.ready