{
  'target_defaults': {
    'include_dirs': [
      '<!(node -e "require(\'nan\')")'
    ],
    'cflags_cc': [
        '-fexceptions',
        '-Wall',
        '-Ofast',
        '-flto',
        '-funroll-loops'
    ],
    'conditions': [
      ['OS=="win"', {
        'defines': [
          'FARMHASH_OPTIONAL_BUILTIN_EXPECT'
        ]
      }],
      ['not "arm" in target_arch', {
        'cflags_cc': [
          '-march=native'
        ],
        'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS': [
            '-march=native',
          ]
        },
      }],
      ['OS=="mac" and target_arch == "arm64"', {
        'xcode_settings': {
          'OTHER_CPLUSPLUSFLAGS': [
            '-mcpu=apple-m1',
          ]
        },

      }]
    ],
    'xcode_settings': {
      'OTHER_CPLUSPLUSFLAGS': [
        '-fexceptions',
        '-Wall',
        '-Ofast',
        '-funroll-loops'
      ]
    },
    'configurations': {
      'Release': {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1,
          }
        }
      }
    }
  },
  'targets': [{
    'target_name': 'farmhash',
    'sources': [
       'src/upstream/farmhash.cc',
       'src/bindings.cc'
    ],
  }, {
    'target_name': 'farmhash-legacy',
    'defines': [
      'FARMHASH_LEGACY'
    ],
    'sources': [
       'src/upstream/farmhash-legacy.cc',
       'src/bindings.cc'
    ],
  },
  ]
}
